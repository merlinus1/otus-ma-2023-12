# ДЗ. Основы работы с Kubernetes (Часть 2)

## Установка Ingress Controller

```shell
kubectl create namespace m && \ 
helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx/ && \ 
helm repo update && helm install nginx ingress-nginx/ingress-nginx --namespace m -f ./ingress/values.yaml
```

## Развертывание

```shell
kubectl apply -f ./k8s/
```

## Тесты

```shell
newman run postman_collection.json
```