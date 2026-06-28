# Guide de Contribution - ScrAPIfY

Merci de votre intérêt pour contribuer à **ScrAPIfY** ! 🙏

## 📋 Table des Matières
- [Code de Conduite](#code-de-conduite)
- [Comment Contribuer](#comment-contribuer)
- [Processus de Pull Request](#processus-de-pull-request)
- [Directives de Code](#directives-de-code)
- [Tests](#tests)

## 🤝 Code de Conduite

Ce projet adhère à un code de conduite pour s'assurer que tout le monde se sent bienvenu. Veuillez lire et respecter notre code de conduite.

## 💡 Comment Contribuer

### Signaler des Bugs
Si vous trouvez un bug :
1. Vérifiez qu'il n'a pas déjà été signalé
2. Créez une **Issue** avec le titre clair
3. Décrivez le problème et comment le reproduire
4. Incluez des captures d'écran si possible

### Suggérer des Améliorations
Pour les nouvelles fonctionnalités :
1. Ouvrez une **Discussion** ou une **Issue**
2. Décrivez clairement l'amélioration
3. Expliquez pourquoi c'est utile
4. Attendez les retours avant de commencer

### Corriger du Code
1. **Fork** le repository
2. Créez une **branch** pour votre changement (`git checkout -b feature/ma-feature`)
3. Faites vos modifications
4. Testez votre code
5. Commitez avec des messages clairs
6. Poussez vers votre fork
7. Ouvrez une **Pull Request**

## 🔄 Processus de Pull Request

1. **Avant de soumettre** :
   - Testez votre code localement
   - Vérifiez que les tests passent
   - Formatez votre code (black, isort)
   - Vérifiez les linting (flake8)

2. **Lors de la soumission** :
   - Donnez un titre clair à votre PR
   - Décrivez vos changements en détail
   - Liez les issues pertinentes
   - Incluez des captures d'écran/vidéos si pertinent

3. **Après la soumission** :
   - Répondez aux commentaires des reviewers
   - Faites les changements demandés
   - Repoussez vos changements

## 📝 Directives de Code

### Style de Code
```python
# Utilisez PEP 8
# - 4 espaces d'indentation
# - Noms explicites
# - Docstrings pour les fonctions
# - Type hints

def function_name(param: str) -> dict:
    """
    Description brève de la fonction
    
    Args:
        param: Description du paramètre
        
    Returns:
        dict: Description du retour
    """
    pass
```

### Format & Linting
```bash
# Formatter avec black
black .

# Trier les imports
isort .

# Linting
flake8 .
```

### Commits
```bash
# Messages de commit clairs
git commit -m "feat: ajouter nouvelle fonctionnalité de scraping"
git commit -m "fix: corriger bug dans le parseur"
git commit -m "docs: mettre à jour la documentation"
git commit -m "test: ajouter tests pour la nouvelle feature"
```

Format recommandé :
- `feat:` - Nouvelle fonctionnalité
- `fix:` - Correction de bug
- `docs:` - Documentation
- `test:` - Tests
- `refactor:` - Refactorisation

## 🧪 Tests

### Écrire des Tests
```python
# tests/scrapers/test_my_scraper.py
import pytest
from scrapy_modules.scrapers.my_scraper import MyScraper

@pytest.mark.asyncio
async def test_scraper_basic():
    scraper = MyScraper()
    result = await scraper.scrape("https://example.com")
    assert result is not None
    assert "title" in result
```

### Lancer les Tests
```bash
# Tous les tests
pytest

# Avec coverage
pytest --cov=api --cov=scrapy_modules

# Tests spécifiques
pytest tests/scrapers/test_my_scraper.py -v

# Arrêt au premier échec
pytest -x
```

## 📚 Documentation

### Docstrings
Utilisez le format Google :
```python
def function(param1: str, param2: int) -> bool:
    """
    Description brève (une ligne).
    
    Description plus longue si nécessaire.
    
    Args:
        param1: Description du premier paramètre
        param2: Description du deuxième paramètre
        
    Returns:
        bool: Description du retour
        
    Raises:
        ValueError: Quand...
        
    Example:
        >>> result = function("test", 42)
        >>> print(result)
        True
    """
    pass
```

## 🔗 Ressources Utiles

- [GitHub Help](https://help.github.com)
- [PEP 8](https://pep8.org/)
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)

## ❓ Questions ?

- Posez vos questions dans les **Discussions**
- Consultez la **Documentation**
- Ouvrez une **Issue** si vous trouvez un problème

---

**Merci encore de contribuer à ScrAPIfY !** ⭐