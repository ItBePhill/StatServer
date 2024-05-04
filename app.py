import flask
import GetResource
from flask import render_template

app = flask.Flask("app")

@app.route('/')
def main():
    return render_template("index.html", cpu_1=GetResource.CPU.Get_CPU_Usage()[0],cpu_2=GetResource.CPU.Get_CPU_Usage()[1],ram_usage=GetResource.RAM.Get_RAM_Usage(),ramu=GetResource.RAM.Get_Used_RAM(),ramt=GetResource.RAM.Get_Total_RAM(),gpu_usage=GetResource.GPU.Get_GPU_Usage(),gpu_mem=GetResource.GPU.Get_GPU_Mem())

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)