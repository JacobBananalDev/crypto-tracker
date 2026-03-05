# 🚀 Crypto Tracker

A backend-first cryptocurrency portfolio tracking platform built with FastAPI, PostgreSQL, SQLAlchemy 2.0, Docker, and a modern Next.js dashboard.

The system tracks cryptocurrency assets, fetches live market data, calculates portfolio value, and displays historical price charts.

This project demonstrates production-style backend architecture, background workers, containerized development, CI/CD pipelines, and infrastructure as code.

## 📸 Preview

(Screenshots will be added later)

Example dashboard:
```bash
Crypto Portfolio Dashboard
Total Value: $12,845.23

BTC     0.52     $10,300
SOL     15.3     $1,200
XRP     300      $1,345
```
## 🏗 Architecture
(Diagram will be added later)
## ✨ Features
### 📊 Portfolio Tracking
- Track cryptocurrency assets
- Calculate portfolio value
-  View asset allocation

### 📈 Market Data
- Automated price updates
- Historical price charts
- Cryptocurrency market tracking

### ⚙️ Backend Engineering
- Versioned REST API (/api/v1)
- SQLAlchemy ORM models
- Database migrations with Alembic
- Background price worker

### 🚀 DevOps
- Docker containerized environment
- GitHub Actions CI/CD pipeline
- Terraform infrastructure configuration

## 🧰 Tech Stack
### 🧠 Backend
| Technology | Purpose |
|-----------|--------|
| FastAPI | High-performance API framework |
| SQLAlchemy 2.0 | ORM |
| PostgreSQL | Relational database |
| Alembic | Database migrations |
| Pydantic | Data validation |
| Python 3.12 | Backend language |
### 🎨 Frontend
| Technology | Purpose |
|-----------|--------|
| Next.js | React framework |
| React	UI | library |
| TypeScript | Type safety |
| TailwindCSS | Styling |
| Charting libraries | Price visualization |
### ☁ Infrastructure
| Technology | Purpose |
|-----------|--------|
| Docker | Containerized services |
| Docker Compose | Local development |
| Terraform | Infrastructure as Code |
| AWS (planned) | Cloud deployment |
| GitHub Actions | CI/CD pipeline |
## 📂 Project Structure
```bash
crypto-tracker
│
├── services
│   └── api
│       ├── app
│       │   ├── api
│       │   │   └── v1
│       │   │       └── routes
│       │   ├── models
│       │   ├── schemas
│       │   ├── services
│       │   ├── db
│       │   └── core
│
├── frontend
│   └── Next.js dashboard
│
├── infra
│   └── terraform
│
└── docker-compose.yml
```
## 🛠 Prerequisites

Before running the project, install the following tools.

### Docker

Install Docker Desktop:

https://www.docker.com/products/docker-desktop/

Verify installation:
```bash
docker --version
docker compose version
```
### Node.js

Required for the Next.js frontend.

Download:

https://nodejs.org

Verify installation:
```bash
node -v
npm -v
```
### Python (optional)

Required if running FastAPI outside Docker.

Download:

https://www.python.org/downloads/

Verify installation:
```bash
python --version
```
### Terraform (optional)

Used for infrastructure deployment.

Download:

https://developer.hashicorp.com/terraform/downloads

Verify installation:
```bash
terraform version
```
## 📦 Installation
### 1️⃣ Clone the repository
```bash
git clone https://github.com/JacobBananalDev/crypto-tracker.git
cd crypto-tracker
```
### 2️⃣ Start the application

Run the entire stack using Docker.
```bash
docker compose up --build
```
Services will start:

| Service | URL |
|--------|-----|
| Frontend | http://localhost:3000 |
| API	| http://localhost:8000 |
| API Docs | http://localhost:8000/docs |
| PostgreSQL |	localhost:5432 |

## 🗄 Database Setup

After the containers start, run migrations.

Open a new terminal:
```bash
docker exec -it crypto-api bash
```
Run:
```bash
alembic upgrade head
```
This creates the database tables.

## 🔌 API Endpoints
Health Check
```bash
GET /api/v1/health
```
Add Cryptocurrency
```bash
POST /api/v1/coins
```
Example request:
```bash
{
  "symbol": "BTC",
  "name": "Bitcoin",
  "image_url": "https://assets.coingecko.com/coins/images/1/large/bitcoin.png"
}
```
Portfolio Value
```bash
GET /api/v1/portfolio/value
```
Price Chart
```bash
GET /api/v1/coins/{symbol}/chart
```
## ⚙️ Background Price Worker

The backend runs a background worker that periodically fetches cryptocurrency prices from CoinGecko.

This enables:
- historical price tracking
- portfolio calculations
- Market trend analysis

## 🔄 CI/CD Pipeline

GitHub Actions automatically:
-  builds backend Docker images
-  builds frontend Docker images
-  pushes images to GitHub Container Registry

## 🏗 Infrastructure (Terraform)

Infrastructure is defined using Terraform.

Planned AWS deployment includes:
- ECS container services
- RDS PostgreSQL database
- Application Load Balancer
- Auto-scaling containers

## 🚧 Future Improvements
- Redis caching for market data
- WebSocket live price updates
- Authentication system
- Multi-portfolio support
- Advanced portfolio analytics

## 👨‍💻 Author
Jacob Bananal <br>
Software Engineer

### 🌐 Portfolio
https://jacobbananal-dev.vercel.app

### 💻 GitHub
https://github.com/JacobBananalDev

### 🔗 LinkedIn
https://www.linkedin.com/in/jacob-bananal-76a418217

## ⭐ If You Found This Helpful

Consider giving the repo a star ⭐
