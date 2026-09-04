# syntax=docker/dockerfile:1
#
# Immagine dell'API (ComitatoFeste.Api), che serve anche il frontend statico da wwwroot.
# Build context = radice del repo. Usata da Render (vedi render.yaml) e da docker-compose.

# --- build ------------------------------------------------------------------
FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build
WORKDIR /src

# Prima i soli .csproj, così il layer di restore resta in cache finché non cambiano.
COPY Src/backend/ComitatoFeste.Api/ComitatoFeste.Api.csproj        Src/backend/ComitatoFeste.Api/
COPY Src/backend/ComitatoFeste.Data/ComitatoFeste.Data.csproj      Src/backend/ComitatoFeste.Data/
COPY Src/backend/ComitatoFeste.Domain/ComitatoFeste.Domain.csproj  Src/backend/ComitatoFeste.Domain/
RUN dotnet restore Src/backend/ComitatoFeste.Api/ComitatoFeste.Api.csproj

# Poi il codice (backend; il frontend è in ComitatoFeste.Api/wwwroot/).
COPY Src/ Src/
RUN dotnet publish Src/backend/ComitatoFeste.Api/ComitatoFeste.Api.csproj \
    -c Release -o /app --no-restore

# --- runtime --------------------------------------------------------------
FROM mcr.microsoft.com/dotnet/aspnet:8.0 AS runtime
WORKDIR /app

# QuestPDF (SkiaSharp) ha bisogno di libfontconfig1 per rendere il PDF del verbale su Linux.
RUN apt-get update \
    && apt-get install -y --no-install-recommends libfontconfig1 \
    && rm -rf /var/lib/apt/lists/*

COPY --from=build /app ./

ENV ASPNETCORE_ENVIRONMENT=Production
# Render inietta PORT a runtime; Program.cs la legge. 8080 è il fallback per l'uso locale.
EXPOSE 8080
ENTRYPOINT ["dotnet", "ComitatoFeste.Api.dll"]
