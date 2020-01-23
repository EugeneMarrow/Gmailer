# Gmailer
You'll need to specify Gmail credentials in conftest.py to run this test.

Test represented in this repo can be performed in the following ways:
1. Run on the local machine.(default)
    Required: Chrome, chromedriver in $PATH.

        pip install -r requirements.txt
        pytest /tests --capture=no

    You may see test progress in opened chrome window.

2. Run remote on local machine:
    Required: Docker, chromedriver in $PATH.

    2.1.Install aerokube/selenoid and selenoid-ui:
    
            curl -s https://aerokube.com/cm/bash | bash \
            && ./cm selenoid start --vnc --tmpfs 128
            docker run -d --name selenoid-ui  \
            --link selenoid                 \
            -p 8080:8080                    \
            aerokube/selenoid-ui --selenoid-uri=http://selenoid:4444

    2.2. Switch to remote driver config in conftest(commented by default)

    2.3. Install packages with:
    
            pip install -r requirements.txt

    2.4. Run with:
    
            pytest /tests --capture=no

      You may see test progress with selenoid-ui by navigating to http://0.0.0.0:8080/#/ with your browser of choise and clicking on current instance.

3. Run remote from docker container:
    Required: Docker.

    3.1.Install aerokube/selenoid and selenoid-ui:

            curl -s https://aerokube.com/cm/bash | bash \
            && ./cm selenoid start --vnc --tmpfs 128
            docker run -d --name selenoid-ui  \
            --link selenoid                 \
            -p 8080:8080                    \
            aerokube/selenoid-ui --selenoid-uri=http://selenoid:4444

    3.2. Switch to remote driver config in conftest(commented by default)
            IMPORTANT! For this config your remote URL should be IP of your host machine.

    2.3. Build docker image with with:
    
            docker build -f Dockerfile -t gmailertest .

    2.4. Start container with:
    
             docker run gmailertest

      Container removes itself after test is done.

      You may see test progress with selenoid-ui by navigating to http://0.0.0.0:8080/#/ with your browser of choise and clicking on current instance.
