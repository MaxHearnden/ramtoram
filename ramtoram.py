def pcinc():
    global pgpoint
    pgpoint+=1
while True:
    line="~"
    pgpoint=0
    ram=[0]*256
    prg=[0]*256
    bus=0
    x=0
    y=0
    acc=0
    overflow=0
    halt=0
    while not line=="":
        try:
            line=raw_input("line "+str(pgpoint))
            prg[pgpoint]=int(line,16)%255
            pgpoint+=1
        except ValueError:
            pass
    pgpoint=0
    try:
        while halt<2:
            if halt==1:
                try:
                    acc=int(raw_input(acc))
                except ValueError:
                    pass
                halt=0
            else:
                currl=prg[pgpoint]
                top=currl/16
                bot=currl%16
                pcinc()
                if top==0:
                    bus=prg[pgpoint]
                    pcinc()
                elif top==1:
                    bus=y
                elif top==2:
                    bus=x
                elif top==3:
                    bus=(x+y)%256
                elif top==4:
                    bus=ram[prg[pgpoint]]
                    pginc()
                elif top==5:
                    bus=ram[y]
                elif top==6:
                    bus=ram[x]
                elif top==7:
                    bus=ram[(x+y)%256]
                elif top==8:
                    bus=overflow
                elif top==9:
                    bus=acc%127
                elif top==10:
                    if acc:
                        bus=0
                    else:
                        bus=1
                elif top==11:
                    bus=acc
                elif top==12:
                    bus=overflow^1
                elif top==13:
                    bus=(acc%127)^1
                elif top==14:
                    if acc:
                        bus=1
                    else:
                        bus=0
                else:
                    bus=acc^255
                if bot==0:
                    halt=bus
                elif bot==1:
                    y=bus
                elif bot==2:
                    x=bus
                elif bot==3:
                    pgpoint=bus
                elif bot==4:
                    ram[prg[pgpoint]]=bus
                    pcinc()
                elif bot==5:
                    ram[y]=bus
                elif bot==6:
                    ram[x]=bus
                elif bot==7:
                    ram[(x+y)%256]=bus
                elif bot==8:
                    acc=bus
                elif bot==9:
                    acc^=bus
                elif bot==10:
                    acc&=bus
                elif bot==11:
                    acc|=bus
                elif bot==12:
                    acc+=bus
                elif bot==13:
                    acc+=(bus^255)+1
                elif bot==14:
                    acc=bus<<1
                else:
                    acc=bus>>1
                if bot in [12,13,14]:
                    overflow=acc/256
                acc%=256
    except KeyboardInterrupt:
        pass
    print(acc)
