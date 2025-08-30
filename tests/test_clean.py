import pandas as pd
from src import clean

def test_simple_clean_removes_nulls():
    df = pd.DataFrame({
        "order_id": [1, 2, 3],
        "rating": [5, None, 4],
        "price": [100, 200, 150]
    })
    df_clean = clean.simple_clean(df)
    # Debe eliminar la fila con rating None
    assert df_clean["rating"].isnull().sum() == 0
    assert len(df_clean) == 2
