import psutil
import time
from collections import defaultdict

class Cor:
    VERDE = "\033[92m"
    AZUL = "\033[94m"
    AMARELO = "\033[93m"
    VERMELHO = "\033[91m"
    ROXO = "\033[95m"
    CIANO = "\033[96m"
    CINZA = "\033[90m"
    NEGRITO = "\033[1m"
    RESET = "\033[0m"

PROTOCOLOS = {
    20: "FTP-DATA", 21: "FTP", 22: "SSH", 23: "TELNET",
    25: "SMTP", 53: "DNS", 80: "HTTP", 110: "POP3",
    123: "NTP", 143: "IMAP", 443: "HTTPS", 465: "SMTPS",
    587: "SMTP-SSL", 993: "IMAPS", 995: "POP3S",
    3306: "MySQL", 3389: "RDP", 5432: "PostgreSQL",
    8080: "HTTP-PROXY", 8443: "HTTPS-ALT",
    27017: "MongoDB", 6379: "Redis", 9200: "Elastic",
    11211: "Memcached", 5222: "XMPP", 5223: "XMPP-SSL",
    5269: "XMPP-SERVER", 6667: "IRC", 6697: "IRC-SSL",
    1883: "MQTT", 8883: "MQTT-SSL", 27015: "Steam",
    25565: "Minecraft", 5060: "SIP", 5061: "SIP-TLS"
}

def protocolo(porta):
    return PROTOCOLOS.get(porta, None)

def servico(porta):
    if porta in (80, 443, 8080, 8443): return "WEB"
    if porta in (25, 110, 143, 465, 587, 993, 995): return "EMAIL"
    if porta in (20, 21, 22, 23, 3389): return "REMOTO"
    if porta in (3306, 5432, 27017, 6379): return "BANCO"
    if porta in (53, 67, 68, 123): return "REDE"
    if porta >= 49152: return "DINÂMICO"
    if porta >= 1024: return "APP"
    return "SISTEMA"

def cabecalho():
    print(f"{Cor.CIANO}{Cor.NEGRITO}╔{'═'*60}╗{Cor.RESET}")
    print(f"{Cor.CIANO}{Cor.NEGRITO}║           🌐 MONITOR DE PROTOCOLOS EM TEMPO REAL           ║{Cor.RESET}")
    print(f"{Cor.CIANO}{Cor.NEGRITO}╚{'═'*60}╝{Cor.RESET}\n")

def rodape(intervalo):
    print(f"\n{Cor.CINZA}{'─'*60}{Cor.RESET}")
    print(f"{Cor.AMARELO}Atualização: {intervalo}s | {Cor.VERMELHO}Ctrl+C{Cor.AMARELO} para sair{Cor.RESET}")

def monitor_compacto():
    cabecalho()
    try:
        while True:
            print("\033[6;0H\033[J", end="")
            conns = psutil.net_connections(kind="inet")
            ativas = [c for c in conns if c.status == "ESTABLISHED" and c.raddr]

            protocolos = defaultdict(int)
            servicos = defaultdict(int)
            ips = defaultdict(int)
            processos = defaultdict(set)

            for c in ativas[:40]:
                if not c.laddr:
                    continue

                p = c.laddr.port
                proto = protocolo(p)
                serv = servico(p)

                if proto:
                    protocolos[proto] += 1
                servicos[serv] += 1

                if c.raddr.ip != "127.0.0.1":
                    ips[c.raddr.ip] += 1

                if c.pid:
                    try:
                        processos[psutil.Process(c.pid).name()].add(proto or "GENÉRICO")
                    except:
                        pass

            hora = time.strftime("%H:%M:%S")
            print(f"{Cor.AMARELO}{Cor.NEGRITO}🕒 {hora}{Cor.RESET}  🔗 {len(ativas)} conexões\n")
            print(f"{Cor.AZUL}{'─'*60}{Cor.RESET}")

            print(f"\n{Cor.NEGRITO}📊 Protocolos:{Cor.RESET}")
            if protocolos:
                for k, v in sorted(protocolos.items(), key=lambda x: x[1], reverse=True):
                    barra = "█" * min(v, 12)
                    print(f"  {Cor.ROXO}{k:15}{Cor.RESET} {Cor.VERDE}{barra:<12}{Cor.RESET} {v}")
            else:
                for k, v in servicos.items():
                    print(f"  {Cor.CIANO}{k:10}{Cor.RESET} → {v}")

            print(f"\n{Cor.NEGRITO}🌍 IPs externos:{Cor.RESET}")
            for ip, c in sorted(ips.items(), key=lambda x: x[1], reverse=True)[:4]:
                cor = Cor.VERMELHO if c > 5 else Cor.AMARELO if c > 2 else Cor.VERDE
                print(f"  {cor}• {ip:<18}{Cor.RESET} {c}")

            print(f"\n{Cor.NEGRITO}⚙️ Processos:{Cor.RESET}")
            for p, pr in sorted(processos.items(), key=lambda x: len(x[1]), reverse=True)[:3]:
                print(f"  {Cor.ROXO}{p[:18]:18}{Cor.RESET} → {', '.join(list(pr)[:2])}")

            rodape(3)
            time.sleep(3)

    except KeyboardInterrupt:
        print(f"\n{Cor.VERDE}{Cor.NEGRITO}✔ Monitor encerrado com sucesso{Cor.RESET}")

if __name__ == "__main__":
    monitor_compacto()
