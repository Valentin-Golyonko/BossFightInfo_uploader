# Auto log uploader for GW2BossFight.info

Main web server https://gw2bossfight.info

### Important notes:

- to run uploader you will need to install a lot of software
- Docker desktop will consume around 2Gb of RAM!
- you must have an account on the main web server in order to use the full functionality of the uploader
- after successful installation, you can connect to the main web server with only one account
- to be able to upload logs, you must confirm your registration on the main web server

### How to install:

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

### How it works:

- TBA

### How to upgrade to a new version:

- TBA

### Support:

- Discord: https://discord.gg/EdCcBvMcDJ

### Code formatter with Black

- `pip install -U black`
- `black app/ celery_scripts/ dj_settings/ help_scripts/`
