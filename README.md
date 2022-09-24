# Auto log uploader for GW2BossFight.info

Main web server https://gw2bossfight.info

### Important notes:

- to run the uploader you will need to install a lot of software
- the Docker desktop consumes about 2 GB of RAM! The uploader consumes an additional 200 MB of RAM.
- you must have an account on the main web server in order to use the full functionality of the uploader
- after successful installation, you can connect to the main web server with only one account
- to be able to upload logs, you must confirm your registration on the main web server

### How to install:

**! the sequence of steps is important, otherwise it will not work !**

1. You will need to install some software to run the uploader:
    - open command line terminal: type `cmd` in windows search and press Enter
    - install Windows subsystem for linux:
        - simple command should work [terminal command]: `wsl --install`
        - if not, follow steps here: https://docs.microsoft.com/en-us/windows/wsl/install-manual
    - install docker desktop: https://www.docker.com/products/docker-desktop/
    - reboot your windows!
    - start Docker desktop
2. Path to logs:
    - go to holder containing ArcDPS logs
    - copy path to **arcdps.cbtlogs** directory
    - path should be like this - `C:\Users\<! YOUR USERNAME !>\Documents\Guild Wars 2\addons\arcdps\arcdps.cbtlogs`
3. Download images:
    - the uploader image [terminal command]: `docker pull bequite/boss-fight-info-uploader:latest`
    - broker image [terminal command]: `docker pull redis:latest`
    - create network [terminal command]: `docker network create --driver bridge bfi-uploader-net`
4. Start containers:
    - start broker
      container [terminal command]: `docker run -d --name broker-redis -p 5672:5672 -p 15672:15672 --restart always --network bfi-uploader-net redis:latest`
    - copy following command to any file editor (_it is one-line
      command_): `docker run -d -v "C:\Users\...\arcdps.cbtlogs:/BossFightInfo_uploader/user_arcdps_logs:ro" --name bfi-uploader -p 8001:8000 --restart always --network bfi-uploader-net bequite/boss-fight-info-uploader:latest`
    - replace path value `-> C:\Users\...\arcdps.cbtlogs <-` with YOURS from step 2.3
    - copy result command to terminal end press enter
5. Check if everything ok:
    - open Docker desktop
    - navigate to 'Containers'
    - you should see running containers,
      ex: <img src="https://github.com/Valentin-Golyonko/BossFightInfo_uploader/blob/master/media/docker_desctop_example.png" alt="docker_desctop_example">
6. Open the uploader in browser:
    - uploader url: http://localhost:8001

### How to start using:

1. after installation done, you should see uploader interfere in your browser http://localhost:8001
2. navigate to "User setting" and enter your "username", "password" and login to the BFi web server
3. after a second you should see updated "username" and "gw2 account name"
4. check if email confirmed

### How it works:

1. main web server stores all uploaded logs
2. on `bfi-uploader` container start, **the uploader synchronizes all logs with main web server**
3. this means you never have to re-upload the logs if something happens to your local logs (ex: a change of log holder)
4. every 15 minutes the uploader checks if you have new logs
5. every 20 minutes the uploader tries to upload new logs to dps.report and BFi main server
6. "Logs list" page displays information about all logs
7. you can hover a "status" badge to see its description
8. [for advanced use only!] to see error logs you may add `-v "C:\bfi_uploader_logs:/BossFightInfo_uploader/logs"` on
   container create, logs will be inside `C:\bfi_uploader_logs`, and DO NOT TOUCH the main_worker.pid file :)

### How to upgrade to a new version:

- pull the latest uploader image from docker hub: `docker pull bequite/boss-fight-info-uploader:latest`
- on the Docker desktop, go to the "Containers" tab and delete the "bfi-uploader" container.
- do step 4.4 from "How to install"

### Current limitations [beta phase]:

- the loader will only look for logs in the current holder with a depth of 1, ex: ".../Xera/20220906-225813.zevtc"

### Global limitations:

- check details here: https://gw2bossfight.info/api/dps_report/upload/
- file path must be < 150 characters
- log file size must be > 1024 bytes
- the uploader will upload a maximum of 10 logs every 20 minutes

### Support:

- Discord: https://discord.gg/EdCcBvMcDJ
