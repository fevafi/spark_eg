import argparse
from utils.process import pipeline

if __name__=="__main__":
    
    print('Spark app building...')
    parser = argparse.ArgumentParser(
                    prog='generic',
                    description='utils for data',
                    epilog='')
    
    parser.add_argument('--source', dest='source', action='store',
                    help='')
    
    parser.add_argument('--sink', dest='sink',
                    help='')
    
    args = parser.parse_args()
    
    pipeline(args)