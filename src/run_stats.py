from run_dssp import run_dssp

def run_stats():
    """Ajaa tilastot DSSP-algoritmille"""
    
    runs = 10000
    b_wins = 0
    i_wins = 0
    e_wins = 0
    for i in range(runs):
        win = run_dssp(difficulty="b", disable_gui=True, running_stats=True)
        if win:
            b_wins += 1
        win = run_dssp(difficulty="i", disable_gui=True, running_stats=True)
        if win:
            i_wins += 1
        win = run_dssp(difficulty="e", disable_gui=True, running_stats=True)
        if win:
            e_wins += 1
            
    print("Beginner wins:", b_wins)
    print("Intermediate wins:", i_wins)
    print("Expert wins:", e_wins)
        
if __name__ == "__main__":
    run_stats()