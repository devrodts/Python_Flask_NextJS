

###### O frontend ainda está em desenvolvimento.

### Auth/Register Python - Flask / Next.Js - TailwindCSS 

1. Backend em Flask (Python) dividido em microserviços (auth_service e user_service)
2. Frontend em Next.js (React)
3. MongoDB para armazenamento de dados
4. Redis para cache/logging
5. Docker para containerização

A documentação incluirá:
- Visão geral das tecnologias
- Arquitetura do projeto
- Endpoints disponíveis (com base no arquivo calls.rest)
- Instruções de instalação e execução
- Detalhes sobre os serviços individuais</think># Documentação do Projeto Flask & React

## Visão Geral

Este projeto implementa uma aplicação web moderna com uma arquitetura de microserviços, utilizando Flask para o backend e Next.js para o frontend. A aplicação é completamente containerizada com Docker, facilitando a configuração do ambiente de desenvolvimento e implantação.

## Tecnologias Utilizadas

### Backend
- **Flask**: Framework web em Python para construção de APIs
- **MongoDB**: Banco de dados NoSQL para armazenamento de dados
- **Redis**: Para cache e armazenamento de logs
- **Flask-JWT-Extended**: Gerenciamento de autenticação via tokens JWT
- **Flask-PyMongo**: Integração do MongoDB com Flask
- **Flask-CORS**: Suporte para Cross-Origin Resource Sharing

### Frontend
- **Next.js 15**: Framework React para renderização de páginas web
- **React 19**: Biblioteca para construção de interfaces de usuário
- **TypeScript**: Superset tipado de JavaScript
- **Tailwind CSS**: Framework CSS para design responsivo

### Infraestrutura
- **Docker & Docker Compose**: Para containerização e orquestração dos serviços
- **Microserviços**: Arquitetura que divide a aplicação em serviços menores e independentes

## Arquitetura do Projeto

O projeto está estruturado em 3 componentes principais:

1. **Auth Service** (Flask) - Porta 5000
   - Responsável pela autenticação e autorização
   - Gerencia registros de usuários e login
   - Emite tokens JWT para acesso protegido

2. **User Service** (Flask) - Porta 5001
   - Gerencia informações de perfil dos usuários
   - Processa solicitações relacionadas a contas de usuário

3. **Frontend** (Next.js) - Porta 3000
   - Interface de usuário responsiva
   - Comunica-se com os serviços de backend via API

Adicionalmente, o projeto utiliza:
- **MongoDB** (Porta 27017): Para persistência de dados
- **Redis** (Porta 6379): Para cache e registro de logs

## Endpoints da API

### Auth Service (http://localhost:5000)

| Método | Endpoint | Descrição | Corpo da Requisição | Resposta |
|--------|----------|-----------|---------------------|----------|
| POST | `/register` | Registra um novo usuário | `{ "username": "user", "password": "pass" }` | Dados do usuário e status |
| POST | `/login` | Autentica um usuário | `{ "username": "user", "password": "pass" }` | Token JWT |
| GET | `/protected` | Endpoint protegido que requer autenticação | N/A | Dados protegidos |

### User Service (http://localhost:5001)

| Método | Endpoint | Descrição | Corpo da Requisição | Resposta |
|--------|----------|-----------|---------------------|----------|
| GET | `/profile/<username>` | Obtém o perfil do usuário | N/A | Dados do perfil |

## Como Executar o Projeto

### Pré-requisitos
- Docker e Docker Compose instalados
- Git para clonar o repositório

### Passos para Execução

1. **Clone o repositório**
   ```bash
   git clone <URL-DO-REPOSITÓRIO>
   cd flask_react
   ```

2. **Inicie os serviços com Docker Compose**
   ```bash
   docker-compose up -d
   ```
   
   Este comando constrói e inicia todos os contêineres definidos no arquivo docker-compose.yml.

3. **Acesse a aplicação**
   - Frontend: http://localhost:3000
   - Auth Service API: http://localhost:5000
   - User Service API: http://localhost:5001

4. **Para parar os serviços**
   ```bash
   docker-compose down
   ```

## Testando a API

Você pode testar os endpoints da API usando a coleção de requisições REST incluída no projeto ou ferramentas como Postman ou curl.

Exemplos de requisições (do arquivo `calls.rest`):

```
### Registrar um novo usuário
POST http://localhost:5000/register
Content-Type: application/json

{
  "username": "testuser",
  "password": "testpass"
}

### Login com o usuário registrado
POST http://localhost:5000/login
Content-Type: application/json

{
  "username": "testuser",
  "password": "testpass"
}

### Acessar um endpoint protegido (substitua <JWT_TOKEN> pelo token recebido no login)
GET http://localhost:5000/protected
Authorization: Bearer <JWT_TOKEN>

### Consultar perfil de usuário
GET http://localhost:5001/profile/testuser
```

## Desenvolvimento

Para desenvolver novos recursos:

1. **Frontend**: Edite os arquivos na pasta `next-frontend/`
2. **Auth Service**: Modifique o código em `flask-backend/auth_service/`
3. **User Service**: Atualize os arquivos em `flask-backend/user_service/`

Após as alterações, reconstrua os contêineres:
```bash
docker-compose build
docker-compose up -d
```

## Solução de Problemas

Se encontrar erros durante a execução do Docker Compose:

1. Verifique se todos os caminhos nos Dockerfiles estão corretos
2. Certifique-se de que os serviços dependentes (Redis, MongoDB) estão rodando
3. Consulte os logs dos contêineres:
   ```bash
   docker-compose logs <nome-do-serviço>
   ```

## Logs e Monitoramento

O projeto usa Redis para armazenar logs. Você pode visualizar os logs através da API ou acessando diretamente o Redis.

