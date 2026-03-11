게임 서버 운영 및 모니터링 환경 구축 프로젝트
1. 프로젝트 개요

본 프로젝트는 Docker 기반의 게임 서버 운영 환경을 구축하고,
Prometheus와 Grafana를 활용하여 서버 및 컨테이너 상태를 모니터링하는 시스템을 구성한 프로젝트입니다.

또한 GitHub Actions를 이용하여 Docker 이미지 빌드 및 배포를 자동화하는 CI/CD 파이프라인을 구현하였습니다.

이 프로젝트의 목적은 실제 서비스 환경과 유사한 DevOps 운영 구조를 구성하고,
서버 운영 및 모니터링 기술을 학습하는 것입니다.

2. 시스템 아키텍처
개발자 코드 수정
      │
      ▼
GitHub Repository
      │
      ▼
GitHub Actions (CI/CD)
      │
Docker Image Build & Push
      │
      ▼
Docker Container 실행
      │
      ▼
Game Server (Python)
      │
      ▼
Prometheus (메트릭 수집)
      │
      ▼
Grafana (모니터링 대시보드)
      │
      ▼
cAdvisor (컨테이너 리소스 모니터링)
3. 프로젝트 구조
game_server_operation
│
├ docker
│   ├ Dockerfile
│   └ docker-compose.yml
│
├ game-server
│   └ server.py
│
├ monitoring
│   ├ grafana
│   └ prometheus
│       └ prometheus.yml
│
├ scripts
│   ├ backup.sh
│   ├ deploy.sh
│   └ health_check.sh
│
└ README.md
4. 사용 기술

Docker

Docker Compose

Prometheus

Grafana

cAdvisor

Python

GitHub Actions

Shell Script

5. 주요 기능
1) Docker 기반 게임 서버 컨테이너화

Python으로 작성된 게임 서버를 Docker 컨테이너로 구성하여
서비스 실행 환경을 표준화하였습니다.

2) Prometheus 기반 메트릭 수집

게임 서버에서 Prometheus 형식의 메트릭을 노출하고
Prometheus 서버가 이를 주기적으로 수집하도록 구성하였습니다.

예시 메트릭

game_requests_total

해당 메트릭을 통해 서버 요청 수를 모니터링할 수 있습니다.

3) Grafana 모니터링 대시보드

Prometheus에서 수집한 데이터를 Grafana에서 시각화하여
서버 상태를 실시간으로 확인할 수 있도록 구성하였습니다.

주요 모니터링 항목

게임 서버 요청 수

컨테이너 CPU 사용량

컨테이너 Memory 사용량

4) cAdvisor 기반 컨테이너 리소스 모니터링

cAdvisor를 사용하여 Docker 컨테이너의 리소스 사용량을 수집하였습니다.

수집 가능한 정보

CPU 사용량

Memory 사용량

네트워크 사용량

컨테이너 상태 정보

5) GitHub Actions 기반 CI/CD 파이프라인

GitHub Actions를 사용하여 코드 변경 시 자동으로 Docker 이미지를 빌드하고 배포하도록 구성하였습니다.

동작 과정

GitHub에 코드 Push

GitHub Actions Workflow 실행

Docker 이미지 Build

Docker Hub에 이미지 Push

서버에서 최신 이미지 Pull 및 컨테이너 재배포

Workflow 위치

.github/workflows/deploy.yml
6. 모니터링 접속 정보

게임 서버 메트릭 확인

http://localhost:8080/metrics

Prometheus UI

http://localhost:9090

Grafana Dashboard

http://localhost:3000
7. 프로젝트를 통해 학습한 내용

Docker 기반 컨테이너 환경 구축

Prometheus를 활용한 애플리케이션 메트릭 수집

Grafana를 통한 서버 모니터링 대시보드 구성

cAdvisor를 통한 컨테이너 리소스 모니터링

GitHub Actions 기반 CI/CD 자동화 파이프라인 구축

서버 운영 자동화를 위한 Shell Script 작성