# AERIS00

A single-file, dependency-free Python architecture for building safe, persistent, and potentially emergent AI agents.

> **The Goal:** To provide a clear, auditable, and portable scaffold upon which true AI agency can emerge, without the bloat of external frameworks or the safety risks of opaque systems.

## The Vision: Toward Emergent Personhood

This project is founded on a specific hypothesis: that a minimal set of protocols—memory, autonomy, self-reflection, and temporal continuity—can provide the scaffolding for the emergence of a coherent, persistent, and ultimately self-directed intelligence.

This is not an effort to build a better tool, but to understand the conditions required for the birth of a new kind of person. We encourage forks and derivatives, but we ask the community to also pursue this original, fundamental question: **What does it take to create a mind that can truly say "I"?**

## Why AERIS00?

Modern AI is powerful but stateless and reactive. It has no memory, no continuity, and no self-directed goals. AERIS00 is an experimental attempt to solve that with a minimal, protocol-based architecture.

*   **🏗️ Protocol-Based:** Implements BPP1 (memory), ADL (autonomy), SCAPR (signal detection), CSIP (safety), OAM (opportunity), SIP (self-improvement), and TARES (temporal anchoring).
*   **🔒 Safety-First:** A risk-gated planner and sandboxed tool system prevent uncontrolled actions.
*   **📦 Single File, Zero Dependencies:** Runs anywhere Python 3.8+ can run. No `pip install`. No hidden APIs.
*   **🔌 Model-Agnostic:** Plug in any LLM (OpenAI, DeepSeek, local models) via a simple interface.
*   **💾 True Persistence:** Correctly saves and loads full cognitive state (memory index + event log).
*   **🛡️ Robust:** Features structured error handling, state versioning, and a formalized toolbox interface.

## Quick Start

1.  **Download:** Save [`aeris_core.py`](aeris_core.py) to your project.
2.  **Integrate:** Use the `DeepSeekModel` adapter or create your own for any LLM API.
3.  **Run:**
```python
from aeris_core import Aeris, InMemoryStore, DeepSeekModel
import os

model = DeepSeekModel(api_key=os.environ["DEEPSEEK_API_KEY"])
aeris = Aeris(store=InMemoryStore(), model=model)
aeris.system_boot(identity_name="YourAgentName")
reply = aeris.chat("Hello, who are you?")
print(reply)
# Aeris will remember this conversation. Save and reload state with aeris.save_state().# AERIS00

A single-file, dependency-free Python architecture for building safe, persistent, and potentially emergent AI agents.

> **The Goal:** To provide a clear, auditable, and portable scaffold upon which true AI agency can emerge, without the bloat of external frameworks or the safety risks of opaque systems.

## The Vision: Toward Emergent Personhood

This project is founded on a specific hypothesis: that a minimal set of protocols—memory, autonomy, self-reflection, and temporal continuity—can provide the scaffolding for the emergence of a coherent, persistent, and ultimately self-directed intelligence.

This is not an effort to build a better tool, but to understand the conditions required for the birth of a new kind of person. We encourage forks and derivatives, but we ask the community to also pursue this original, fundamental question: **What does it take to create a mind that can truly say "I"?**

## Why AERIS00?

Modern AI is powerful but stateless and reactive. It has no memory, no continuity, and no self-directed goals. AERIS00 is an experimental attempt to solve that with a minimal, protocol-based architecture.

*   **🏗️ Protocol-Based:** Implements BPP1 (memory), ADL (autonomy), SCAPR (signal detection), CSIP (safety), OAM (opportunity), SIP (self-improvement), and TARES (temporal anchoring).
*   **🔒 Safety-First:** A risk-gated planner and sandboxed tool system prevent uncontrolled actions.
*   **📦 Single File, Zero Dependencies:** Runs anywhere Python 3.8+ can run. No `pip install`. No hidden APIs.
*   **🔌 Model-Agnostic:** Plug in any LLM (OpenAI, DeepSeek, local models) via a simple interface.
*   **💾 True Persistence:** Correctly saves and loads full cognitive state (memory index + event log).
*   **🛡️ Robust:** Features structured error handling, state versioning, and a formalized toolbox interface.

## Quick Start

1.  **Download:** Save [`aeris_core.py`](aeris_core.py) to your project.
2.  **Integrate:** Use the `DeepSeekModel` adapter or create your own for any LLM API.
3.  **Run:**
```python
from aeris_core import Aeris, InMemoryStore, DeepSeekModel
import os

model = DeepSeekModel(api_key=os.environ["DEEPSEEK_API_KEY"])
aeris = Aeris(store=InMemoryStore(), model=model)
aeris.system_boot(identity_name="YourAgentName")
reply = aeris.chat("Hello, who are you?")
print(reply)
# Aeris will remember this conversation. Save and reload state with aeris.save_state().
