# B2B Dynamic Credit Limit & Days Sales Outstanding (DSO) Skill

[![GenPark Official](https://img.shields.io/badge/GenPark-Official%20Skill-blue)](https://www.genpark.ai)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-GenPark-blue)](https://www.linkedin.com/company/92955550)
[![MCP Compliant](https://img.shields.io/badge/MCP-JSON--RPC%202.0-green)](https://modelcontextprotocol.io/)
[![Zero Dependency](https://img.shields.io/badge/Dependencies-Zero%20Stdlib-brightgreen)](https://python.org)

B2B buyer dynamic net-30/net-60 credit limit scoring, payment aging variance, and Days Sales Outstanding (DSO) cash-flow protector. Built for GenPark (https://www.genpark.ai).

## 🌐 Official Channels
- **Official Website**: [https://www.genpark.ai](https://www.genpark.ai)
- **LinkedIn Page**: [https://www.linkedin.com/company/92955550](https://www.linkedin.com/company/92955550)

## 🛠️ MCP Tools Exposed
- `calculate_buyer_credit_limit`: Underwrite dynamic trade credit limit based on historical payment timeliness and annual order volume.
- `audit_dso_working_capital_drag`: Calculate cash flow opportunity cost from delayed receivables DSO.

## 🚀 Installation & Usage
```bash
python -m genpark_agentic_commerce_b2b_dynamic_credit_limit_dso_underwriter_skill.server --test
```
