from elliot.run import run_experiment
import argparse

parser = argparse.ArgumentParser(description="Run training and evaluation.")
parser.add_argument('--model', type=str, default='ngcf')
parser.add_argument('--dataset', type=str, default='movielens')
args = parser.parse_args()

run_experiment(f"config_files/{args.model}/{args.dataset}.yml")