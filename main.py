from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse
import pandas as pd
from utils.data_processing import filter_data, generate_graph, generate_summary_graph, generate_population_growth_graph, generate_comparation__graph 
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

# Cargar datos iniciales
data ={
    "poblacion_desempleo": [
        {
            "Período": 2019,
            "Población Colombia": 48322678,
            "Población en edad de trabajar": 36926240,
            "Porcentaje población en edad de trabajar": 76.4,
            "Población económicamente activa": 23911939,
            "Tasa general de participación": 64.8,
            "Desocupados Número de personas": 2602126,
            "Tasa de desempleo": 10.9
        },
        {
            "Período": 2020,
            "Población Colombia": 49260971,
            "Población en edad de trabajar": 37771268,
            "Porcentaje población en edad de trabajar": 76.7,
            "Población económicamente activa": 22820925,
            "Tasa general de participación": 60.4,
            "Desocupados Número de personas": 3771799,
            "Tasa de desempleo": 16.5
        },
        {
            "Período": 2021,
            "Población Colombia": 49941374,
            "Población en edad de trabajar": 38432467,
            "Porcentaje población en edad de trabajar": 77.0,
            "Población económicamente activa": 23654636,
            "Tasa general de participación": 61.5,
            "Desocupados Número de personas": 3262895,
            "Tasa de desempleo": 13.8
        },
        {
            "Período": 2022,
            "Población Colombia": 50495179,
            "Población en edad de trabajar": 38996571,
            "Porcentaje población en edad de trabajar": 77.2,
            "Población económicamente activa": 24813516,
            "Tasa general de participación": 63.6,
            "Desocupados Número de personas": 2781336,
            "Tasa de desempleo": 11.2
        },
        {
            "Período": 2023,
            "Población Colombia": 51027876,
            "Población en edad de trabajar": 39547229,
            "Porcentaje población en edad de trabajar": 77.5,
            "Población económicamente activa": 25364698,
            "Tasa general de participación": 64.1,
            "Desocupados Número de personas": 2576305,
            "Tasa de desempleo": 10.2
        }
    ]
}

df = pd.DataFrame(data["poblacion_desempleo"])


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    # Generar gráfico general de todos los años
    graph = generate_summary_graph(df)
    population_graph = generate_population_growth_graph(df)
    comparation_graph = generate_comparation__graph(df)
    return templates.TemplateResponse("index.html", {
        "request": request,
        "graph": graph,
        "population_graph": population_graph,
        "comparation_graph": comparation_graph
})



@app.get("/filter", response_class=HTMLResponse)
async def filter_data_route(request: Request, year: str = None):
    if not year:  # Si 'year' está vacío o es None
        return RedirectResponse(url="/")
 
    try:
        year = int(year)  # Intentar convertir a entero
    except ValueError:
        return RedirectResponse(url="/")  # Redirigir si no es un número válido
    
    # Filtrar los datos según el año
    filtered_data = filter_data(df, year)
    # Generar gráfico filtrado por año
    graph = generate_graph(filtered_data)
    return templates.TemplateResponse("index.html", {
        "request": request,
        "data": filtered_data.to_dict('records'),
        "graph": graph,
        "selected_year": year  # Pasar el año seleccionado
    })

