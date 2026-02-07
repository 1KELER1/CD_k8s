#   FastAPI приложение (GitOps Consumer)



## Описание
- **FastAPI приложение** с автоматической сборкой Docker образов
- **Цель**: CI/CD пайплайн → GHCR → ArgoCD Image Updater → EKS
- Инфраструктура: [infra_argo_code](https://github.com/1KELER1/infra_argo_code)
- Докер образы: [ghcr.io/1keler1/cd_k8s](https://github.com/users/1keler1/packages/container/package/cd_k8s)


# Требования
| Инструмент | Версия        | Зачем              |
| ---------- | ------------- | ------------------ |
| Git        | 2.30+         | Клонирование + PR  |
| Docker     | 20.10+        | Локальная проверка |
| Python     | 3.12          | Lint + dev         |

# CI/CD
| Шаг | Действие            | Инструмент     | Время          |
| --- | ------------------- | -------------- | -------------- |
| 1   | PR → CD_k8s         | Developer      | 1 сек          |
| 2   | Lint проверка       | GitHub Actions | 30 сек         |
| 3   | Merge PR → main     | Developer      | Ручное         |
| 4   | Lint + Docker Build | GitHub Actions | 30 сек         |
| 5   | Push GHCR           | Docker         | 1 мин          |
| 6   | Прямой push         | Image Updater  | 10 сек         |
| 7   | ArgoCD Sync         | Kubernetes     | 30 сек         |

# Настройка текущего репозитория
Settings → Secrets and variables → Actions → New repository secret:

- Name: PAT_TOKEN 
- Value: ghp_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
- Права:  delete:packages , repo , workflow , write:packages

