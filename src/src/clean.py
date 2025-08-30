import pandas as pd

def simple_clean(df: pd.DataFrame) -> pd.DataFrame:
    """Ejemplo: quitar filas con valores nulos en rating."""
    return df.dropna(subset=["rating"])

if __name__ == "__main__":
    # Carga un CSV de ejemplo
    df = pd.DataFrame({
        "order_id": [1, 2, 3],
        "rating": [5, None, 4],
        "price": [100, 200, 150]
    })
    print("Antes de limpiar:", len(df))
    df_clean = simple_clean(df)
    print("Después de limpiar:", len(df_clean))
