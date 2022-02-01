# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2021-2022 Valory AG
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# ------------------------------------------------------------------------------

"""IO operations for the APY skill."""

import joblib
import pandas as pd
from pmdarima.pipeline import Pipeline

from packages.valory.skills.apy_estimation_abci.tools.etl import TRANSFORMED_HIST_DTYPES


def save_forecaster(path: str, forecaster: Pipeline) -> None:
    """Save a `pmdarima` forecaster.

    :param path: path to store the forecaster.
    :param forecaster: the `pmdarima` forecasting model.
    """
    joblib.dump(forecaster, path)


def load_forecaster(path: str) -> Pipeline:
    """Load a `pmdarima` forecaster.

    :param path: path to store the forecaster.
    :return: a `pmdarima.pipeline.Pipeline`.
    """
    return joblib.load(path)


def load_hist(path: str) -> pd.DataFrame:
    """Load the already fetched and transformed historical data.

    :param path: the path to the historical data.
    :return: a dataframe with the historical data.
    """
    pairs_hist = pd.read_csv(path).astype(TRANSFORMED_HIST_DTYPES)

    # Convert the `blockTimestamp` to a pandas datetime.
    pairs_hist["blockTimestamp"] = pd.to_datetime(
        pairs_hist["blockTimestamp"], unit="s"
    )

    return pairs_hist
