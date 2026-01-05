# 🌐 Monitor de Protocolos de Rede em Tempo Real (CLI)

Ferramenta de monitoramento de protocolos de rede em tempo real, desenvolvida em **Python**, que analisa conexões ativas diretamente a partir do sistema operacional.

O projeto fornece uma visão clara e contínua da atividade de rede, exibindo protocolos utilizados, categorias de serviço, IPs externos e processos associados, tudo em uma interface de terminal limpa, organizada e visualmente informativa.

---

## ✨ Funcionalidades

### 📡 Monitoramento
- Monitoramento em tempo real de conexões ativas (**ESTABLISHED**)
- Atualização automática em intervalo padrão de **3 segundos**
- Encerramento seguro da execução com **Ctrl + C**

---

### 🧠 Análise de Rede
- Identificação automática de protocolos de rede, incluindo:
  - HTTP / HTTPS
  - SSH
  - DNS
  - SMTP, FTP, entre outros
- Detecção dos **IPs externos mais ativos**
- Associação direta das conexões aos **processos do sistema operacional**

---

### 🗂 Classificação de Serviços
As conexões são classificadas automaticamente por tipo de serviço:
- **WEB**
- **EMAIL**
- **BANCO DE DADOS**
- **ACESSO REMOTO**
- **REDE**

---

### 🖥 Interface CLI
- Interface de linha de comando **dinâmica e responsiva**
- Uso de **cores ANSI** para melhor leitura
- **Barras gráficas** para visualização do volume de atividade
- **Indicadores visuais com emojis** para rápida interpretação

---

## 🎯 Objetivo do Projeto

Este projeto tem como objetivo oferecer uma solução **leve, direta e eficiente** para:
- Monitoramento local de conexões de rede
- Diagnóstico rápido de tráfego
- Estudo de protocolos e serviços
- Apoio ao aprendizado em **redes e segurança da informação**
