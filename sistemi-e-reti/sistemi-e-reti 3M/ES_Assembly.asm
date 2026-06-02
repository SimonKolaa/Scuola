org 100h

    vect DB 3,1,9,5,8,3,3,3,9,4
    ris DB 0
    cont1 DB 10

    lea si, [vect]

    mov bl, 0

INIZIO_CICLO:
    mov al, [si]
    cmp al, 3
    jne FINE_IF
    inc bl

FINE_IF:
    inc si
    loop INIZIO_CICLO

    mov [ris], bl

    mov ah, 4Ch
    int 21h

    ret



