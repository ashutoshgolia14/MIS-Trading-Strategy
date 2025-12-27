# MIS Algo Trading System
## Unit Test Specification (UTS)

**Status:** 🟡 Draft (Formal)  
**Derived From:**  
- Software Requirements Specification (SRS – Frozen)  
- Detailed Software Design (DSD – Frozen)

**Test Rule:** Every Software Requirement (SWR) shall have at least one corresponding unit test.  
**Change Policy:** Modifications allowed until UTS inspection & freeze.

---

## 1. Purpose

This document defines the **Unit Test Specification (UTS)** for the MIS Algo Trading System.

The UTS:
- Maps each **Software Requirement (SWR)** to one or more **unit test cases**
- Defines test intent, inputs, expected outputs, and pass criteria
- Ensures deterministic and isolated verification of software behavior

---

## 2. Unit Test Principles

1. **Requirement-based testing** – tests are derived strictly from SWRs
2. **Isolation** – external dependencies are mocked or stubbed
3. **Determinism** – identical inputs must always produce identical outputs
4. **Repeatability** – tests must be re-runnable without side effects
5. **Traceability** – every test traces back to a single SWR

---

## 3. Unit Test Environment Assumptions

- Market data inputs are simulated
- Broker interface is fully mocked
- System time can be controlled or injected
- Persistence layer uses in-memory or test storage

---

## 4. Unit Test Cases

### 4.1 Strategy Evaluation & Trading Logic

#### UT-TRD-001
**Verifies:** Renko-only evaluation trigger
- **Covers:** SWR-TRD-001
- **Preconditions:** Strategy Core initialized
- **Input:** Non-Renko tick event
- **Expected Result:** No trade decision generated
- **Pass Criteria:** Decision = HOLD

---

#### UT-TRD-002
**Verifies:** Higher-timeframe directional bias application
- **Covers:** SWR-TRD-002
- **Input:** Snapshot with bullish higher-timeframe bias
- **Expected Result:** Trade decision aligns with bias

---

#### UT-TRD-003
**Verifies:** Lower-timeframe confirmation logic
- **Covers:** SWR-TRD-004
- **Input:** Snapshot failing momentum/volatility criteria
- **Expected Result:** Trade entry rejected

---

#### UT-TRD-004
**Verifies:** Deterministic behavior under rapid Renko events
- **Covers:** SWR-TRD-003
- **Input:** Multiple Renko bricks generated in the same processing cycle
- **Expected Result:** Only the latest snapshot is processed; all older pending snapshots are explicitly discarded
- **Pass Criteria:** Exactly one trade decision evaluated, based on the latest snapshot

---

### 4.2 Timing & Session Control

#### UT-TIM-001
**Verifies:** Entry window enforcement
- **Covers:** SWR-TIM-001
- **Input:** Trade attempt outside entry window
- **Expected Result:** Entry blocked

---

#### UT-TIM-002
**Verifies:** End-of-day force close
- **Covers:** SWR-TIM-002
- **Input:** Open position at force close time
- **Expected Result:** Exit triggered

---

### 4.3 Renko Processing

#### UT-RNK-001
**Verifies:** Renko brick generation
- **Covers:** SWR-RNK-001
- **Input:** Price movement exceeding brick size
- **Expected Result:** Correct Renko brick generated

---

### 4.4 Order Execution & Broker Interaction

#### UT-EXE-001
**Verifies:** Market order placement
- **Covers:** SWR-EXE-001
- **Input:** Valid trade decision
- **Expected Result:** Market order sent to broker mock and successful ExecutionResult returned
- **Pass Criteria:** ExecutionResult indicates success and contains expected order metadata

---

#### UT-EXE-002
**Verifies:** Spread validation logic
- **Covers:** SWR-EXE-002
- **Input:** Spread above configured threshold
- **Expected Result:** Order not placed and ExecutionResult indicates rejection
- **Pass Criteria:** ExecutionResult indicates failure with spread-rejection reason

---

#### UT-EXE-003
**Verifies:** Partial fill handling
- **Covers:** SWR-EXE-003
- **Input:** Partial fill response from broker mock
- **Expected Result:** No retry issued

---

### 4.5 Risk & Position Management

#### UT-RSK-001
**Verifies:** Risk-based position sizing
- **Covers:** SWR-RSK-001
- **Input:** Equity and stop distance
- **Expected Result:** Quantity matches expected calculation

---

#### UT-RSK-002
**Verifies:** Margin usage enforcement
- **Covers:** SWR-RSK-002
- **Input:** Trade exceeding margin cap
- **Expected Result:** Trade blocked

---

#### UT-RSK-003
**Verifies:** Fixed daily equity usage
- **Covers:** SWR-RSK-003
- **Input:** Equity change during day
- **Expected Result:** Calculations still use initial equity

---

### 4.6 Persistence & Recovery

#### UT-REC-001
**Verifies:** State persistence
- **Covers:** SWR-REC-001
- **Input:** Active symbol state
- **Expected Result:** State saved and reloadable

---

#### UT-REC-002
**Verifies:** Recovery and reconciliation
- **Covers:** SWR-REC-002
- **Input:** Persisted state vs broker-reported position mismatch
- **Expected Result:** Broker state takes precedence

---

### 4.7 Logging & Monitoring

#### UT-LOG-001
**Verifies:** Trade event logging
- **Covers:** SWR-LOG-001
- **Input:** Trade decision event
- **Expected Result:** Log entry with correct category and payload

---

## 5. Traceability Summary

| Software Requirement | Unit Test ID(s) |
|---------------------|----------------|
| SWR-TRD-001 | UT-TRD-001 |
| SWR-TRD-002 | UT-TRD-002 |
| SWR-TRD-004 | UT-TRD-003 |
| SWR-TRD-003 | UT-TRD-004 |
| SWR-TIM-001 | UT-TIM-001 |
| SWR-TIM-002 | UT-TIM-002 |
| SWR-RNK-001 | UT-RNK-001 |
| SWR-EXE-001 | UT-EXE-001 |
| SWR-EXE-002 | UT-EXE-002 |
| SWR-EXE-003 | UT-EXE-003 |
| SWR-RSK-001 | UT-RSK-001 |
| SWR-RSK-002 | UT-RSK-002 |
| SWR-RSK-003 | UT-RSK-003 |
| SWR-REC-001 | UT-REC-001 |
| SWR-REC-002 | UT-REC-002 |
| SWR-LOG-001 | UT-LOG-001 |

---

## 6. Next Steps

1. Inspect Unit Test Specification
2. Resolve findings (if any)
3. Freeze UTS
4. Implement unit tests
5. Execute unit testing

---

**End of Unit Test Specification**

