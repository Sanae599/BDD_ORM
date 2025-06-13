# Gestion des Sessions de Formation - CF-Tech

## Description

Ce projet vise à moderniser la gestion des informations concernant les sessions de formation, les salles, les formateurs et les apprenants au sein du centre de formation CF-Tech. Nous remplaçons les fichiers Excel et l'ERP vieillissant par une base de données relationnelle robuste, utilisant SQLAlchemy/SQLModel pour l'ORM, Alembic pour les migrations de base de données, et Pydantic pour la validation stricte des données.

## Fonctionnalités

- Gestion des sessions de formation
- Gestion des salles et des ressources
- Gestion des formateurs et de leurs disponibilités
- Gestion des apprenants et de leurs inscriptions
- Validation stricte des données avec Pydantic
- Migrations de base de données avec Alembic

## Prérequis

Avant de commencer, assurez-vous d'avoir installé les éléments suivants :

- Python 3.8 ou supérieur
- PostgreSQL (ou tout autre SGBD compatible avec SQLAlchemy)
- pip (pour l'installation des dépendances Python)

## Installation

1. Clonez le dépôt sur votre machine locale :

   ```bash
   git clone https://github.com/votre-utilisateur/cf-tech.git
   cd cf-tech
