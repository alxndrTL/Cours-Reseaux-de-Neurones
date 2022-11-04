def parcours(G, s0, traitement):
    '''
    effectue le parcours en largeur du graphe G à partir du sommet s0.
    '''
    
	aTraiter = []
	dejaVu = []
    
    aTraiter.append(s0)
    dejaVu.append(s0)
    
    while aTraiter:
        s = aTraiter[0]
        aTraiter = aTraiter[1:]
        
        # début du traitement de s
        traitement(s)
        
        for t in G[s]:
            if t not in dejaVu:
                aTraiter.append(t)
                dejaVu.append(t)
                
        # fin du traitement de s