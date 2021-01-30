
print("**************DEVIS****************")
DB = [
    [100, 'LOTUS'], [150, 'RASOIR']
    ,[400,'COCA'],[50,'BISCUIT'],
    [500, 'ORANGINA'], [200, 'EAU'],
    [350,'PRESERVATIF'],[ 700,'CIGARETTE'],
    [500, 'AMPOULE'], [50, 'PILE'],
    [ 200,'LAIT'],[100,'STYLO'],
    [500,'CODYS'],[ 300,'SAVON'],
    [200,'MOUCHOIR'],[ 25,'BONBON'],
    [500,'CAHIER'],[ 150,'PAIN'],[1000,'INSECTISIDE'],
    [100,'MILO'],[50,'NESCAFE'],
    [200,'CACHE NEZ'],[ 50,'SUCRE'],

    ]
ART=[]
A=0
r=1
def prod():


    global ART
    global r
    T=0
    E = 0
    Q=0
    global DB

    while r==1:



        E=input("DONNER LE NOM DU PRODUIT\n")
        Q=int(input("DONNER LA QUANTITE \n"))
        for i,N in DB:
            if E==N:

                print("_______________________________________")

                print("PRIX UNITAIRE: {} FCFA".format(i))
                T=T+(i*Q)
                print("TOTAL :{}FCFA".format(T))

        r= int(input("TAPEZ 1 POUR AJOUTER UN NOUVEAU PRODUIT..\n"))

ART.extend([DB])
def aff():
    # SI LA FONCTION aff() NE MARCHE PAS AVEC LA CMD SIMPLE UTILISER UN IDE
    for i in range(len(DB)):

        print("{}.".format(i))
        print(ART)
        break

print("_______________________________________")
print(" LA SAISIR SE FAIT EN GRAND CARACTERE")
print("_______________________________________")
print("TAPEZ 1 POUR ACHETER UN PRODUIT")
print("TAPEZ 2 POUR AFFICHER LES MONTANT DE PRODUIT")
A=int(input("ENTREZ VOTRE CHOIX 1/2 "))

if A ==1:

    prod()
elif A==2:

    aff()
