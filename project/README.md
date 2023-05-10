<h1>
<code><img height="40" src="https://img.icons8.com/?size=512&id=KwebQJATkcPg&format=png"></code>
Satellite Telemetry Interview Project 
<code><img height="40" src="https://img.icons8.com/?size=512&id=KwebQJATkcPg&format=png"></code>
</h1>

---

<h2> <u> Synopsis </u> </h2>

As part of the interview process, a hands-on technical assessment of skillsets has been required. 
The assessment shall be conducted against a list of requirements provided, and graded based on performance.
The following code has been presented for the purpose of satisfaction of the aforementioned requirement(s).

---
<h2> <u> Specifications Sheet </u> </h2>

| Requirement    | Synopsis                                                               |
|----------------|------------------------------------------------------------------------|
| 1              | Application will conduct conditional logic on battery state            |
| 2              | Application will conduct conditional logic on thermal state            |
| 3              | Application will Import/Export data manually                           |
| 4              | Application will generate notifications of Out of Bound states         |
| 5              | Application will generate JSON based formatted outputs                 |
| 6              | Application will provide JSON based formatted output in specified form |
---

<h2> <u> Getting Started </u> </h2>
To deploy the project, please follow the following instructions:

First, navigate to the microservices by changing to the <b> MICROSERVICES </b> directory via command line, and repeating the following command within <b> SATELLITE-1 </b> directory:
> gunicorn --bind 0.0.0.0:9010 wsgi &

Second, repeating the following command within <b> SATELLITE-2 </b> directory:
> gunicorn --bind 0.0.0.0:9011 wsgi &

Next, to deploy the base environment, change directories to the parent project directory <b>ENLIGHTEN</b>, and run the following command:
> docker-compose up -d --build
---
Once you have completed building the environment, go to the following URL
> 127.0.0.1:1337/login

Use the following credentials to authenticate:
> username: test
<br>
> password: Satellite1!

Once you have successfully authenticated, go to the following URL:
- Operational UI - http://127.0.0.1:1337/ops/
- Task Results - http://127.0.0.1:1337/admin/django_celery_results/taskresult/
- Admin Import/Export Events - http://127.0.0.1:1337/admin/UI/event/
- API Events Datapoint - http://127.0.0.1:1337/api/event/

To verify services are running:

API JSON Output:
> curl -X GET 127.0.0.1:1337/api/event/

Satellite-1 is generating data: 
> curl -X GET 0.0.0.0:9010

Satellite-2 is generating data:
> curl -X GET 0.0.0.0:9011

---
<h3> <u> Overview </u></h3>

> <b> Project Status - Current </b>

| Component           | Description                                                                                                                  |
|---------------------|------------------------------------------------------------------------------------------------------------------------------|
| Frontend            | ![nyan!](https://gitlab.com/gitlab-org/gitlab/badges/main/coverage.svg?job=karma&key_text=Frontend+Coverage&key_width=130)   |
| Backend             | ![nyan!](https://gitlab.com/gitlab-org/gitlab/badges/main/coverage.svg?job=karma&key_text=Backend+Coverage&key_width=130)    |
| Database            | ![nyan!](https://gitlab.com/gitlab-org/gitlab/badges/main/coverage.svg?job=karma&key_text=dbsqlite3+Coverage&key_width=130)  |
| Automations         | ![nyan!](https://gitlab.com/gitlab-org/gitlab/badges/main/coverage.svg?job=karma&key_text=Celery+Coverage&key_width=130)     |
| Caching             | ![nyan!](https://gitlab.com/gitlab-org/gitlab/badges/main/coverage.svg?job=karma&key_text=Redis+Coverage&key_width=130)      |  
| Datalake            | ![nyan!](https://gitlab.com/gitlab-org/gitlab/badges/main/coverage.svg?job=karma&key_text=Elastic+Coverage&key_width=130)    |  
| Frameworks          | ![nyan!](https://gitlab.com/gitlab-org/gitlab/badges/main/coverage.svg?job=karma&key_text=Frameworks+Coverage&key_width=130) |
| Containerized       | ![status](https://img.shields.io/badge/status-up-brightgreen)                                                                |
| SAST/DAST Complete  | ![status](https://img.shields.io/badge/status-down-red)                                                                      |  
| Production Deploy   | ![status](https://img.shields.io/badge/status-down-red)                                                                      |  
| State               | ![status](https://img.shields.io/badge/status-up-brightgreen)                                                                |
| Multi-Cloud Support | ![status](https://img.shields.io/badge/status-up-brightgreen)                                                                | 
---
<h2>  <u> Technical Index </u> </h2>

The following items are for technical reference in case of bugs, issues, troubleshooting, or general reference.

---
<h2> <u> Known Issues </u> </h2>

<h4> Weak Default Credentials </h4>

> Its a default credential, shared across the interwebs. They ain't Fort Knox blueprints. Change the credential if its a concern with the following:
<br>
> http://127.0.0.1:1337/admin/password_change/
<br>
> And yes, its http. Yea, I know. Sir, this is a Wendy's.

<h4> Microservices Not Dockerized </h4>

> There is currently an issue with the microservices effectively deploying due to docker CMD interpretation of gunicorn --chdir option flag, and docker directory in general. In order to simplify, --chdir commands were included, and outreach has been done for guidance for work arounds. In an effort to avoid complexity of docker-compose file, microservices are currently manually deployed.

<h4> Duplication of py package downloads

> Due to issues with the microservices not being deployed within docker-compose environment, packages are being duplicated for the local python environment in order for the microservices to be run locally outside of the docker container.

<h4> Profiles reference issues

> References aren't loading properly when navigating to profile or edit profile. Profile wasn't part of the requirement, nor is there time to add it. Removing it from the base module is also time consuming, so in the interests of saving additional time, its been left in place as broken until such a time as to be remediated. 
---
<h2> <u> Troubleshooting  </u></h2>
In the event the docker-compose file fails to build with the error max limit reached, it is likely you have too many unused containers & images.
The issue can be solved by pruning them, by running the following command(s):

- Prune unused docker systems
> docker system prune -a

- Prune unused docker containers
> docker container prune -a

- Prune unused docker images
> docker container image -a
---

<h2> Technology References </h2>

| Technologies          | Link                                                                     |
|-----------------------|--------------------------------------------------------------------------|
| Bootstrap             | [Bootstrap](https://github.com/Fallenour/Quiz-Management-System-Django)  |
| CSS                   | [CSS](https://github.com/Fallenour/Quiz-Management-System-Django)        |
| Javascript            | [Javascript](https://github.com/Fallenour/Quiz-Management-System-Django) |
| Chart.js              | [Chart.js](https://www.chartjs.org/docs/latest/)                         |
| Highcharts.js         | [Highcharts.js](https://www.highcharts.com)                              |
| Django                | [Django](https://www.djangoproject.com)                                  |
| Django Rest Framework | [Django Rest Framework](https://www.django-rest-framework.org)           |
| Django Signals        | [Django Signals](https://docs.djangoproject.com/en/4.2/topics/signals/)  |
| Python                | [Python](https://www.python.org)                                         |
| PostgreSQL            | [PostgreSQL](https://www.postgresql.org)                                 |
| Flask                 | [Flask](https://flask.palletsprojects.com/en/2.3.x/)                     |
| Celery                | [Celery](https://docs.celeryq.dev/en/stable/)                            |
| Docker                | [Docker](https://docs.docker.com)                                        |
| Docker-Compose        | [Docker-Compose](https://docs.docker.com/compose/)                       |
| Redis                 | [Redis](https://redis.io/docs/)                                                                |
---
<h2> <u> Tech Stack </u> </h2>

| Features              | Technologies                                        |
|-----------------------|-----------------------------------------------------|
| Front End             | Bootstrap, CSS, Javascript, Chart.js, Highcharts.js |
| Backend               | Django, Python, PostgreSQL                          |
| Microservices         | Flask                                               |
| Async Task Management | Celery                                              |
| Containerization      | Docker Compose                                      |
| Messaging & Channels  | Django Signals                                      |
| Caching               | Redis                                               |
| API                   | Django Rest Framework                               |
---
<h2> <u> Software Bill of Sale </u> </h2>
<b> Author</b>: Logan H.
<br>
<b> Creation Date</b>: 05-09-2023
<br>
<b> Format</b>: U.S. National Telecommunications & Information Administration (NTIA)

| Supplier Name         | Component Name        | Version       | Unique Identifiers | Dependencies       |
|-----------------------|-----------------------|---------------|--------------------|--------------------|
| Bootstrap             | Bootstrap             | 4.1.1         | <placeholder>      | <placeholder>      |
| CSS                   | CSS                   | 4.1.1         | <placeholder>      | <placeholder>      |
| Javascript            | JQuery                | 3.4.1         | <placeholder>      | <placeholder>      |
| Chart.js              | Chart.js              | 2.4.0         | <placeholder>      | <placeholder>      |
| Chartist              | Chartist.js           | 0.11.0        | <placeholder>      | <placeholder>      |
| Django                | Django                | 4.1.5         | <placeholder>      | <placeholder>      |
| Django Rest Framework | Django Rest Framework | 3.14.0        | <placeholder>      | <placeholder>      |
| Python                | Python                | <placeholder> | <placeholder>      | <placeholder>      |
| Flask                 | Flask                 | 2.3.1         | <placeholder>      | <placeholder>      |
| Celery                | Celery                | 5.2.7         | <placeholder>      | <placeholder>      |
| Docker-Compose        | Docker-Compose        | 2.2.0         | <placeholder>      | <placeholder>      |
| Redis                 | Redis                 | 4.4.2         | <placeholder>      | <placeholder>      |
| PyPi                  | amqp                  | 5.1.1         | <placeholder>      | <placeholder>      |
| PyPi                  | aniso8601             | 9.0.1         | <placeholder>      | <placeholder>      |
| PyPi                  | asgiref               | 3.6.0         | <placeholder>      | <placeholder>      |
| PyPi                  | async-timeout         | 4.0.2         | <placeholder>      | <placeholder>      |
| PyPi                  | attrs                 | 21.2.0        | <placeholder>      | <placeholder>      |
| PyPi                  | billiard              | 3.6.4.0       | <placeholder>      | <placeholder>      |
| PyPi                  | blinker               | 1.6.2         | <placeholder>      | <placeholder>      |
| PyPi                  | celery                | 5.2.7         | <placeholder>      | <placeholder>      |
| PyPi                  | certifi               | 2022.12.7     | <placeholder>      | <placeholder>      |
| PyPi                  | charset-normalizer    | 3.0.1         | <placeholder>      | <placeholder>      |
| PyPi                  | click                 | 8.1.3         | <placeholder>      | <placeholder>      |
| PyPi                  | click-didyoumean      | 0.3.0         | <placeholder>      | <placeholder>      |
| PyPi                  | click-plugins         | 1.1.1         | <placeholder>      | <placeholder>      |
| PyPi                  | click-repl            | 0.2.0         | <placeholder>      | <placeholder>      |
| PyPi                  | defusedxml            | 0.7.1         | <placeholder>      | <placeholder>      |
| PyPi                  | diff-match-patch      | 20200713      | <placeholder>      | <placeholder>      |
| PyPi                  | Django                | 4.1.5         | <placeholder>      | <placeholder>      |
| PyPi                  | django-celery-beat    | 2.4.0         | <placeholder>      | <placeholder>      |
| PyPi                  | django-celery-results | 2.4.0         | <placeholder>      | <placeholder>      |
| PyPi                  | django-import-export  | 3.0.2         | <placeholder>      | <placeholder>      |
| PyPi                  | django-timezone-field | 5.0           | <placeholder>      | <placeholder>      |
| PyPi                  | djangorestframework   | 3.14.0        | <placeholder>      | <placeholder>      |
| PyPi                  | et-xmlfile            | 1.1.0         | <placeholder>      | <placeholder>      |
| PyPi                  | factory-boy           | 3.2.1         | <placeholder>      | <placeholder>      |
| PyPi                  | Faker                 | 16.6.1        | <placeholder>      | <placeholder>      |
| PyPi                  | Flask                 | 2.3.1         | <placeholder>      | <placeholder>      |
| PyPi                  | Flask-RESTful         | 0.3.9         | <placeholder>      | <placeholder>      |
| PyPi                  | flower                | 1.2.0         | <placeholder>      | <placeholder>      |
| PyPi                  | gunicorn              | 20.1.0        | <placeholder>      | <placeholder>      |
| PyPi                  | humanize              | 4.5.0         | <placeholder>      | <placeholder>      |
| PyPi                  | idna                  | 3.4           | <placeholder>      | <placeholder>      |
| PyPi                  | importlib-metadata    | 4.6.4         | <placeholder>      | <placeholder>      |
| PyPi                  | iniconfig             | 1.1.1         | <placeholder>      | <placeholder>      |
| PyPi                  | itsdangerous          | 2.1.2         | <placeholder>      | <placeholder>      |
| PyPi                  | Jinja2                | 3.1.2         | <placeholder>      | <placeholder>      |
| PyPi                  | kombu                 | 5.2.4         | <placeholder>      | <placeholder>      |
| PyPi                  | MarkupPy              | 1.14          | <placeholder>      | <placeholder>      |
| PyPi                  | MarkupSafe            | 2.1.2         | <placeholder>      | <placeholder>      |
| PyPi                  | more-itertools        | 8.10.0        | <placeholder>      | <placeholder>      |
| PyPi                  | odfpy                 | 1.4.1         | <placeholder>      | <placeholder>      |
| PyPi                  | openpyxl              | 3.0.10        | <placeholder>      | <placeholder>      |
| PyPi                  | packaging             | 21.3          | <placeholder>      | <placeholder>      |
| PyPi                  | pip                   | 23.1.2        | <placeholder>      | <placeholder>      |
| PyPi                  | pluggy                | 0.13.0        | <placeholder>      | <placeholder>      |
| PyPi                  | prometheus-client     | 0.16.0        | <placeholder>      | <placeholder>      |
| PyPi                  | prompt-toolkit        | 3.0.36        | <placeholder>      | <placeholder>      |
| PyPi                  | py                    | 1.10.0        | <placeholder>      | <placeholder>      |
| PyPi                  | Pygments              | 2.11.2        | <placeholder>      | <placeholder>      |
| PyPi                  | pyparsing             | 2.4.7         | <placeholder>      | <placeholder>      |
| PyPi                  | pytest                | 6.2.5         | <placeholder>      | <placeholder>      |
| PyPi                  | python-crontab        | 2.7.1         | <placeholder>      | <placeholder>      |
| PyPi                  | python-dateutil       | 2.8.2         | <placeholder>      | <placeholder>      |
| PyPi                  | pytz                  | 2022.7.1      | <placeholder>      | <placeholder>      |
| PyPi                  | PyYAML                | 6.0           | <placeholder>      | <placeholder>      |
| PyPi                  | redis                 | 4.4.2         | <placeholder>      | <placeholder>      |
| PyPi                  | requests              | 2.28.2        | <placeholder>      | <placeholder>      |
| PyPi                  | setuptools            | 59.6.0        | <placeholder>      | <placeholder>      |
| PyPi                  | six                   | 1.16.0        | <placeholder>      | <placeholder>      |
| PyPi                  | sqlparse              | 0.4.3         | <placeholder>      | <placeholder>      |
| PyPi                  | tablib                | 3.3.0         | <placeholder>      | <placeholder>      |
| PyPi                  | toml                  | 0.10.2        | <placeholder>      | <placeholder>      |
| PyPi                  | tornado               | 6.2           | <placeholder>      | <placeholder>      |
| PyPi                  | tzdata                | 2022.7        | <placeholder>      | <placeholder>      |
| PyPi                  | urllib3               | 1.26.14       | <placeholder>      | <placeholder>      |
| PyPi                  | vine                  | 5.0.0         | <placeholder>      | <placeholder>      |
| PyPi                  | wcwidth               | 0.2.6         | <placeholder>      | <placeholder>      |
| PyPi                  | Werkzeug              | 2.3.2         | <placeholder>      | <placeholder>      |
| PyPi                  | wheel                 | 0.37.1        | <placeholder>      | <placeholder>      |
| PyPi                  | xlrd                  | 2.0.1         | <placeholder>      | <placeholder>      |
| PyPi                  | xlwt                  | 1.3.0         | <placeholder>      | <placeholder>      |
| PyPi                  | zipp                  | 1.0.0         | <placeholder>      | <placeholder>      |

---
