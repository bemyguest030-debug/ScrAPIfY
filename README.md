# 🕷️ ScrAPIfY - Web Scraping & Product Positioning Platform

**ScrAPIfY** est une application intelligente de web scraping qui collecte et analyse les données pour positionner votre produit et adresser la bonne solution à la bonne audience.

## 🎯 Fonctionnalités Principales

- ✅ **Scraping Multi-Sources** : E-commerce, réseaux sociaux, sites concurrents
- ✅ **Analyse de Sentiment** : Comprendre la perception du marché
- ✅ **Positionnement Produit** : Analyse prix, features, marché cible
- ✅ **Dashboard Interactif** : Visualisation des données en temps réel
- ✅ **API REST** : Intégration facile avec vos systèmes
- ✅ **Export Données** : CSV, JSON, PDF
- ✅ **Détection Concurrents** : Surveiller vos concurrents
- ✅ **Tendances Marché** : Analyser les évolutions

## 🏗️ Architecture

```
ScrAPIfY/
├── scrapy_modules/          # Modules de scraping
│   ├── scrapers/           # Scrapers spécialisés
│   ├── parsers/            # Parseurs de données
│   └── pipelines/          # Pipelines de traitement
├── api/                    # Backend FastAPI
│   ├── routes/             # Endpoints API
│   ├── models/             # Models de données
│   └── services/           # Services métier
├── database/               # Configuration DB
├── config/                 # Configuration
├── tests/                  # Tests unitaires
└── docs/                   # Documentation
```

## 🚀 Installation & Démarrage Rapide

### Prérequis
- Python 3.8+
- pip / Poetry
- PostgreSQL (optionnel, SQLite par défaut)

### Installation

```bash
# Cloner le repository
git clone https://github.com/bemyguest030-debug/ScrAPIfY.git
cd ScrAPIfY

# Créer un environnement virtuel
python -m venv venv
source venv/bin/activate  # Sur Windows: venv\Scripts\activate

# Installer les dépendances
pip install -r requirements.txt

# Configurer l'environnement
cp .env.example .env
# Éditer .env avec vos configurations
```

### Démarrer l'API

```bash
python main.py
```

L'API sera disponible sur `http://localhost:8000`

Accédez à la documentation interactive: `http://localhost:8000/docs`

## 📚 Documentation API

### Endpoints Principaux

#### 1. Scraper une URL
```bash
curl -X POST "http://localhost:8000/api/v1/scrape" \
  -H "Content-Type: application/json" \
  -d "{
    \"url\": \"https://example.com\",
    \"scraper_type\": \"ecommerce\",
    \"analyze_sentiment\": true
  }"
```

#### 2. Analyser un Produit
```bash
curl -X POST "http://localhost:8000/api/v1/analyze/product" \
  -H "Content-Type: application/json" \
  -d "{
    \"product_name\": \"My Product\",
    \"sources\": [\"amazon\", \"ebay\"],
    \"market_segment\": \"tech\"
  }"
```

#### 3. Surveiller les Concurrents
```bash
curl -X POST "http://localhost:8000/api/v1/monitor/competitors" \
  -H "Content-Type: application/json" \
  -d "{
    \"competitors\": [\"competitor1.com\", \"competitor2.com\"],
    \"metrics\": [\"price\", \"reviews\"],
    \"frequency\": \"daily\"
  }"
```

## 🔧 Configuration

### .env
```
# Database
DATABASE_URL=postgresql://user:password@localhost/scrapify

# API
API_HOST=0.0.0.0
API_PORT=8000
DEBUG=true

# Scraping
MAX_WORKERS=5
REQUEST_TIMEOUT=10
USER_AGENT=ScrAPIfY/1.0

# Services externes
SENTIMENT_API_KEY=your_key_here
```

## 📊 Exemples d'Utilisation

### Python Client
```python
import requests

api_url = "http://localhost:8000/api/v1"

# Scraper une URL
response = requests.post(f"{api_url}/scrape", json={
    "url": "https://example.com",
    "scraper_type": "ecommerce"
})
print(response.json())

# Analyser un produit
response = requests.post(f"{api_url}/analyze/product", json={
    "product_name": "My Product",
    "sources": ["amazon"]
})
print(response.json())
```

## 🛠️ Technologies Utilisées

- **Backend** : FastAPI, Uvicorn
- **Scraping** : BeautifulSoup, Selenium, Requests, Scrapy
- **Database** : SQLAlchemy, PostgreSQL
- **Analyse** : TextBlob, NLTK, Pandas
- **Export** : Pandas, ReportLab (PDF)
- **Tests** : Pytest

## 🧪 Tests

```bash
# Lancer tous les tests
pytest

# Tests avec coverage
pytest --cov=api --cov=scrapy_modules

# Tests spécifiques
pytest tests/scrapers/ -v
```

## 📈 Performance

- ⚡ Scraping parallélisé (5+ sites simultanément)
- 💾 Caching des résultats
- 🔄 Pagination automatique
- 📊 Traitement batch optimisé

## 🔒 Sécurité

- ✅ Respect du robots.txt
- ✅ Rate limiting intégré
- ✅ User-Agent spoofing responsable
- ✅ Validation des données d'entrée
- ✅ JWT pour l'API

## 📄 Licence

MIT License - Libre d'utilisation

## 🤝 Contribution

Les contributions sont bienvenues ! Consultez [CONTRIBUTING.md](CONTRIBUTING.md) pour plus de détails.

## 📞 Support

- 📧 Email : support@scrapify.dev
- 🐛 Issues : https://github.com/bemyguest030-debug/ScrAPIfY/issues
- 💬 Discussions : https://github.com/bemyguest030-debug/ScrAPIfY/discussions

---

**Made with ❤️ by ScrAPIfY Team**