# Snowflake Analytics with dbt, Airflow, and Metabase

This repository provides a modular analytics pipeline using **Snowflake**, **dbt**, **Apache Airflow**, and **Metabase** for end-to-end data transformation, orchestration, and visualization.

---

## 🚀 Features

- **dbt Models**: SQL-based transformations on Snowflake.
- **Airflow DAGs**: Workflow scheduling and orchestration.
- **Metabase**: Interactive dashboards and visual analytics.
- **Dockerized Setup**: One-command environment provisioning using Docker Compose.
- **Snowflake Integration**: Secure and scalable cloud data warehouse support.

---

## 📁 Project Structure

- `models/`: dbt transformation models.
- `macros/`: Reusable SQL logic for dbt.
- `dags/`: Airflow DAGs to trigger dbt runs.
- `profiles/`: dbt Snowflake profile configuration.
- `init/`: Environment or db setup scripts.
- `Dockerfile.airflow`: Custom image for Airflow.
- `docker-compose.yml`: Stack configuration for dbt, Airflow, and Metabase.
- `dbt_project.yml`: dbt project config.
- `packages.yml`: External dbt packages.
- `requirements.txt`: Python dependencies.

---

## 🛠️ Setup Instructions

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/anooprp/snowflake_analytics_dbt.git
   cd snowflake_analytics_dbt
   ```

2. **Configure dbt Profile**:

   - Update `profiles/profiles.yml` with the correct profile name (e.g., `test_profile`, `snowflake_analytics`) and target settings.

3. **Add Environment Variables**:

   - Copy the provided `.env.example` to `.env`:

     ```bash
     cp .env.example .env
     ```

   - Fill in all Snowflake and Airflow connection variables.

4. **Launch Services**:

   ```bash
   docker-compose up --build
   ```

5. **Access Services**:

   - **Airflow UI**: [http://localhost:8080](http://localhost:8080)
   - **Metabase UI**: [http://localhost:3000](http://localhost:3000)

6. **Metabase Configuration**:

   - On first launch, complete Metabase setup.
   - Connect to the Snowflake DB used by dbt.
   - Use dbt models as data sources for dashboards.

---

## 🔐 Environment Variables

See `.env.example` for all required variables:

```dotenv
# .env for snowflake_analytics (prod-like)
SNOWFLAKE_ACCOUNT=your_account
SNOWFLAKE_USER=your_user
SNOWFLAKE_PASSWORD=your_password
SNOWFLAKE_ROLE=your_role

# .env for test_profile
SNOWFLAKE_DEV_ACCOUNT=your_dev_account
SNOWFLAKE_DEV_USER=your_dev_user
SNOWFLAKE_DEV_PASSWORD=your_dev_password
SNOWFLAKE_DEV_ROLE=your_dev_role

# airflow connection
AIRFLOW_CONN_SNOWFLAKE_CLEANUP='snowflake://user:password@account/DBT_ANALYTICS/CORE?warehouse=COMPUTE_WH&role=ACCOUNTADMIN'
AIRFLOW_CONN_SNOWFLAKE_DEV_CLEANUP='snowflake://user:password@account/TEST_DB/TEST_SCHEMA?warehouse=COMPUTE_WH&role=ACCOUNTADMIN'
```

> ⚠️ Do **not** commit `.env`. Only `.env.example` should be versioned.

---

## 📖 Serving dbt Documentation

After running dbt_pipeline_prod dag, the documentation is saved in the `/usr/app/target` directory.

You can serve the generated docs using a lightweight static file server:

### Using Python’s built-in HTTP server login to dbt server



```bash
docker exec -it snowflake_analytics_dbt bash

cd /usr/app/target
python3 -m http.server 8081
This will serve your dbt docs at http://localhost:8081.