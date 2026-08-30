from __future__ import annotations
import argparse, json
from .io import read_csv
from .metrics import summarize_p2, score_p3, score_p4be
from .locks import sha256_file
from .reporting import lint_selective_audit_reporting, p4be_selective_summary

def main(argv=None):
    p = argparse.ArgumentParser(prog="aido-cav")
    sub = p.add_subparsers(dest="cmd", required=True)

    s=sub.add_parser("score-p4be"); s.add_argument("csv")
    s=sub.add_parser("score-p3"); s.add_argument("csv")
    s=sub.add_parser("summarize-p2"); s.add_argument("--arm-a",required=True); s.add_argument("--arm-b",required=True); s.add_argument("--arm-c",required=True)
    s=sub.add_parser("sha256"); s.add_argument("file")
    s=sub.add_parser("lint-report"); s.add_argument("file")
    sub.add_parser("public-summary")

    a=p.parse_args(argv)
    if a.cmd=="score-p4be":
        out=score_p4be(read_csv(a.csv))
    elif a.cmd=="score-p3":
        out=score_p3(read_csv(a.csv))
    elif a.cmd=="summarize-p2":
        out=summarize_p2(read_csv(a.arm_a),read_csv(a.arm_b),read_csv(a.arm_c))
    elif a.cmd=="sha256":
        out={"file":a.file,"sha256":sha256_file(a.file)}
    elif a.cmd=="lint-report":
        out={"issues":lint_selective_audit_reporting(open(a.file,encoding="utf-8").read())}
    elif a.cmd=="public-summary":
        print(p4be_selective_summary()); return 0
    print(json.dumps(out,indent=2,ensure_ascii=False))
    return 0

if __name__=="__main__":
    raise SystemExit(main())
