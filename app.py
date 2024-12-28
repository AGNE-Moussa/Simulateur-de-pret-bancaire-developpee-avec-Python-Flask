from flask import Flask,render_template,request

app=Flask("__name__")  #cela veut dire on utilise une application flask

@app.route("/")
def affiche(): #FONCTION POUR AFFICHER
    return render_template("entree.html")

@app.route("/calcul",methods=['POST'])
def traite(): #FONTION POUR CALCUL
    vmpret=request.form['vmpret'] #Le module de demandes vous permet d'envoyer des requêtes HTTP en utilisant Python.
                                  # La requête HTTP renvoie un objet de réponse avec toutes les données de réponse

    vtia = request.form['vtia']
    vn = request.form['vn']
    mpret=int(vmpret)
    tia=float(vtia)
    n=int (vn)
    tim=tia/1200
    mtmens=(mpret * tim)/(1 - 1/((1 + tim)**(12*n)))
    mglobal= 12*mtmens*n

    return render_template("sortie.html", mpret=mpret, n=n, tia=tia, mtmens=mtmens , mglobal=mglobal)
#return render template renvoie les informations au niveau de sortie.html

if __name__=='__main__':
    app.run(debug=True) #c'est ce qui permet d'exécuter