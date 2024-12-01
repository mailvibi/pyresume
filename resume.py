import pystache 
import json
import argparse

def read_file(filename):
    with open(filename, "r") as f:
        b = f.read()
        return b

def write_file(filename, data):
    with open(filename, "w") as f:
#        f.write(bytes(data, "utf-8"))
        f.write(data)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--template", required=True)
    ap.add_argument("--json", required=True)
    ap.add_argument("--output", required=True)

    args = ap.parse_args()
    htm_template_file = args.template
    resume_json = args.json
    resume_html = args.output

    tmpl = read_file(htm_template_file)
    res_jsn = read_file(resume_json)
    res_jsn = json.loads(res_jsn)
    res_html = pystache.render(tmpl, res_jsn)
    write_file(resume_html, res_html)

if __name__ == "__main__":
    main()