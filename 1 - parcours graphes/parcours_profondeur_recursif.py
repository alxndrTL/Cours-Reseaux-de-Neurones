def parcours(G, s0, traitement):
    '''
    effectue le parcours en profondeur du graphe G à partir du sommet s0.
    '''
    
	
    dejaVu = []
    
    def parcours_r(s, G):
        dejaVu.append(s)
        
        # début du traitement de s
        traitement(s)

        for t in G[s]:
            if t not in dejaVu:
                parcours_r(t, G)
        
        # fin du traitement de s
        
    parcours(G, s0)