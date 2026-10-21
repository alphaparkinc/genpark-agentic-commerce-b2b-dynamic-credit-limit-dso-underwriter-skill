# -*- coding: utf-8 -*-
"""B2B Dynamic Credit Limit & DSO Underwriter for GenPark Agentic Commerce."""
import json
from typing import Dict, Any

class B2BDynamicCreditLimitDSOUnderwriter:
    @staticmethod
    def calculate_buyer_credit_limit(annual_order_volume_usd: float, average_days_to_pay: float, net_terms_days: int) -> Dict[str, Any]:
        monthly_run_rate = annual_order_volume_usd / 12.0
        timeliness_factor = 1.2 if average_days_to_pay <= net_terms_days else max(0.4, 1.0 - ((average_days_to_pay - net_terms_days) / 30.0))
        credit_limit = round(monthly_run_rate * 1.5 * timeliness_factor, 2)
        return {"annual_volume_usd": annual_order_volume_usd, "recommended_credit_limit_usd": credit_limit, "payment_risk": "EXCELLENT" if timeliness_factor >= 1.0 else "DELINQUENT_RISK"}

    @staticmethod
    def audit_dso_working_capital_drag(total_receivables_usd: float, total_annual_credit_sales_usd: float) -> Dict[str, Any]:
        dso = round((total_receivables_usd / total_annual_credit_sales_usd) * 365, 1)
        capital_cost = round(total_receivables_usd * 0.08, 2)
        return {"current_dso_days": dso, "total_receivables_usd": total_receivables_usd, "annual_working_capital_cost_at_8pct_usd": capital_cost}
