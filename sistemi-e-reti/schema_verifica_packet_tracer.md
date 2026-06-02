# Schema rapido Cisco Packet Tracer (verifica)

## Ordine consigliato

1.  Piano IP\
2.  VLAN\
3.  Trunk\
4.  Router / Gateway\
5.  EIGRP\

------------------------------------------------------------------------

## Piano di indirizzamento

Esempio:

-   VLAN 10 → `192.168.10.0/26` → gateway `192.168.10.1`
-   VLAN 20 → `192.168.10.64/26` → gateway `192.168.10.65`

Promemoria rapido:

-   `/26` = `255.255.255.192`
-   wildcard EIGRP = `0.0.0.63`

------------------------------------------------------------------------

## VLAN (switch)

### Creazione VLAN

``` bash
enable
configure terminal
vlan 10
vlan 20
```

### Porte access

``` bash
interface fa0/1
switchport mode access
switchport access vlan 10
```

### Trunk

``` bash
interface fa0/24
switchport mode trunk
switchport trunk allowed vlan 10,20
```


------------------------------------------------------------------------

## Router-on-a-stick (802.1Q)

### Attivazione interfaccia

``` bash
interface g0/0
no shutdown
```

### Subinterface

``` bash
interface g0/0.10
encapsulation dot1Q 10
ip address 192.168.10.1 255.255.255.192

interface g0/0.20
encapsulation dot1Q 20
ip address 192.168.10.65 255.255.255.192
```

**Da ricordare:**

-   `dot1Q` = numero VLAN
-   l'interfaccia fisica va attivata
-   di solito l'IP va sulle subinterface

------------------------------------------------------------------------

## DHCP (solo se serve)

``` bash
ip dhcp pool LAN10
network 192.168.10.0 255.255.255.192
default-router 192.168.10.1
```

------------------------------------------------------------------------

## EIGRP

### Config minima

``` bash
router eigrp 100
network 192.168.10.0 0.0.0.63
network 192.168.10.64 0.0.0.63
no auto-summary
```

**Importante:**

-   stesso AS su tutti i router
-   le rotte EIGRP compaiono con **D**


------------------------------------------------------------------------
