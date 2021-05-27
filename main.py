import herramientasMate  as hm
import class as c
import herramientas as h
import SEL as s

def app():

    localKs = []
    localbs = []
    Kv = []
    b = []
    Tv = []

    print("--------MEF 2D--------")
    print("Transferencia de calor")
    
    d = c.Mesh()
    filename = "test2"

    h.leerMallayCondiciones(d, filename)
    print("Datos obtenidos correctamente\n********************\n")

    s.crearSistemasLocales(d, localKs, localbs)
    print("******************************\n")

    hm.PrimeroCero(Kv, d.getSize(c.Sizes.NODES.value))
    hm.TercerCero(b, d.getSize(c.Sizes.NODES.value))

    s.ensamblaje(d, localKs, localbs, Kv, b)
    print("******************************\n")

    s.applyNeumann(d, b)
    print("******************************\n")

    s.applyDirichlet(d, Kv, b)
    print("******************************\n")

    hm.TercerCero(Tv, len(b))
    s.calculate(Kv, b, Tv)

    h.writeResults(d, Tv, filename)

app()