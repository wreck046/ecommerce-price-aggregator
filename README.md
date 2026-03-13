# Ecommerce Price Aggregator

Project untuk scraping harga marketplace dan menampilkan analisis harga.

## Features

- Scrape Shopee products
- Store data in PostgreSQL
- FastAPI REST API
- Streamlit dashboard

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

## Architecture

Scraper → PostgreSQL → FastAPI → Streamlit
