# Ecommerce Price Aggregator

Project untuk scraping harga marketplace dan menampilkan analisis harga.

## Features

- Multi-Marketplace Scraper (Shopee + Tokopedia)
- Data Storage with PostgreSQL
- FastAPI REST API
- Streamlit Analytics Dashboard
- Docker Deployment

## Architecture

Scraper → PostgreSQL → FastAPI → Dashboard

## Tech Stack

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Streamlit
- Playwright

## Installation

pip install -r requirements.txt

## Run Scraper

python -m scripts.run_scraper

## Run API

uvicorn src.app.api.main:app --reload

## Run Dashboard

streamlit run src/app/dashboard/app.py
