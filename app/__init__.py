body {
  font-family: Arial, sans-serif;
  background: linear-gradient(180deg, #f5f1ea 0%, #eef7f9 100%);
  margin: 0;
  color: #1e293b;
}

.topbar {
  background: linear-gradient(135deg, #0f172a, #0f766e);
  color: white;
  padding: 22px 30px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.topbar h2 {
  margin: 0;
  font-size: 1.8rem;
}

.topbar small {
  color: #dbeafe;
}

.topbar-actions {
  display: flex;
  gap: 10px;
  align-items: center;
}

.container {
  padding: 24px;
  max-width: 1200px;
  margin: 0 auto;
}

.tabs {
  display: flex;
  gap: 12px;
  margin-bottom: 20px;
  flex-wrap: wrap;
}

.tab {
  background: #e2e8f0;
  color: #0f172a;
  padding: 10px 18px;
  border-radius: 999px;
  cursor: pointer;
  font-weight: bold;
  transition: all 0.2s ease;
}

.tab.active {
  background: #0f766e;
  color: white;
}

.tab-panel {
  display: none;
}

.card {
  background: rgba(255, 255, 255, 0.94);
  border-radius: 16px;
  padding: 20px;
  box-shadow: 0 10px 30px rgba(15, 23, 42, 0.08);
  margin-bottom: 18px;
}

.card h3 {
  margin-top: 0;
}

.row {
  display: flex;
  gap: 16px;
  flex-wrap: wrap;
}

.col {
  flex: 1;
  min-width: 180px;
}

.col.wide {
  flex: 2;
}

label {
  display: block;
  font-weight: 600;
  margin-top: 10px;
  margin-bottom: 4px;
}

input, select, textarea, button {
  width: 100%;
  box-sizing: border-box;
  border-radius: 10px;
  border: 1px solid #cbd5e1;
  padding: 10px 12px;
  font-size: 14px;
}

textarea {
  min-height: 80px;
}

button {
  background: linear-gradient(135deg, #f59e0b, #d97706);
  color: white;
  border: none;
  font-weight: 700;
  cursor: pointer;
}

button.outline {
  background: transparent;
  border: 1px solid white;
  color: white;
}

button.mini {
  padding: 8px 12px;
  font-size: 12px;
  border-radius: 8px;
  margin-right: 6px;
}

button.mini.danger {
  background: #dc2626;
}

table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 10px;
}

th, td {
  padding: 12px 10px;
  text-align: left;
  border-bottom: 1px solid #e2e8f0;
}

th {
  color: #475569;
  font-size: 12px;
  text-transform: uppercase;
  letter-spacing: 0.06em;
}

.status-pill {
  display: inline-block;
  padding: 6px 10px;
  border-radius: 999px;
  background: #e0f2fe;
  color: #0f172a;
  font-size: 12px;
  font-weight: 700;
}

.mini-badge {
  border-radius: 999px;
  background: #ecfeff;
  color: #0f172a;
  display: inline-block;
  padding: 10px 14px;
  margin-top: 8px;
  font-weight: 600;
}

#chart {
  display: flex;
  gap: 16px;
  align-items: end;
  min-height: 180px;
  margin-top: 20px;
}

.bar-group {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
}

.bar {
  width: 100%;
  background: linear-gradient(180deg, #f59e0b, #ef4444);
  border-radius: 10px 10px 0 0;
  color: white;
  display: flex;
  align-items: end;
  justify-content: center;
  font-weight: bold;
  min-height: 30px;
  padding-bottom: 8px;
}

.empty-state {
  color: #64748b;
}

.filters {
  margin-bottom: 12px;
}

@media (max-width: 700px) {
  .topbar { flex-direction: column; align-items: flex-start; gap: 12px; }
  .container { padding: 14px; }
}
