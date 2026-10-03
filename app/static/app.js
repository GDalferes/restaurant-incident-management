<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>The Rusty Anchor</title>
  <link rel="stylesheet" href="/static/styles.css" />
</head>
<body>
  <div class="topbar">
    <div>
      <h2>The Rusty Anchor</h2>
      <small>Kitchen safety & incident desk</small>
    </div>
    <div class="topbar-actions">
      <button id="roleToggle" class="outline">Manager View</button>
    </div>
  </div>

  <div class="container">
    <div class="tabs">
      <div class="tab active" data-tab="incidents">Incidents</div>
      <div class="tab" data-tab="assignments">Assignments</div>
      <div class="tab" data-tab="tips">Customer Tips</div>
      <div class="tab" data-tab="insights">Insights</div>
    </div>

    <div id="incidents" class="tab-panel">
      <div class="card">
        <h3>Submit Incident</h3>
        <form id="incidentForm">
          <div class="row">
            <div class="col wide">
              <label>Summary</label>
              <textarea name="summary" required placeholder="Example: Grease flare at fryer station"></textarea>
            </div>
            <div class="col">
              <label>Station</label>
              <select name="station_id" id="stationSelect"></select>
            </div>
            <div class="col">
              <label>Staff</label>
              <select name="staff_id" id="staffSelect"></select>
            </div>
          </div>
          <div class="row" style="margin-top:12px;">
            <div class="col">
              <label>Type</label>
              <input name="incident_type" value="Kitchen Safety" />
            </div>
            <div class="col">
              <label>Item</label>
              <input name="item_name" placeholder="Fryer A" />
            </div>
            <div class="col">
              <label>Status</label>
              <select name="status">
                <option>Open</option>
                <option>In Review</option>
                <option>Resolved</option>
              </select>
            </div>
          </div>
          <div style="margin-top:16px;">
            <button type="submit">Add Incident</button>
          </div>
        </form>
      </div>

      <div class="card">
        <h3>Incident Search & Filter</h3>
        <div class="row filters">
          <div class="col"><input id="searchInput" placeholder="Search summary or type" /></div>
          <div class="col"><select id="stationFilter"><option value="">All stations</option></select></div>
          <div class="col"><input id="startDate" type="date" /></div>
          <div class="col"><input id="endDate" type="date" /></div>
        </div>
        <table>
          <thead>
            <tr><th>Summary</th><th>Type</th><th>Station</th><th>Status</th><th>Action</th></tr>
          </thead>
          <tbody id="incidentTable"></tbody>
        </table>
      </div>
    </div>

    <div id="assignments" class="tab-panel" style="display:none;">
      <div class="card">
        <h3>Assignment Review</h3>
        <table>
          <thead>
            <tr><th>Staff</th><th>Station</th><th>Shift</th><th>Status</th><th>Action</th></tr>
          </thead>
          <tbody id="assignmentTable"></tbody>
        </table>
      </div>
    </div>

    <div id="tips" class="tab-panel" style="display:none;">
      <div class="card">
        <h3>Customer Tip Line (No Login)</h3>
        <form id="tipForm">
          <div class="row">
            <div class="col wide">
              <label>Tip Description</label>
              <textarea name="description" required placeholder="I noticed a leak in the walk-in cooler and the smell of fryer oil was strong."></textarea>
            </div>
            <div class="col">
              <label>Location</label>
              <input name="location" placeholder="Back Kitchen" required />
            </div>
          </div>
          <div class="row" style="margin-top:12px;">
            <div class="col">
              <label>Guest Name</label>
              <input name="guest_name" placeholder="Anonymous" />
            </div>
            <div class="col">
              <label>Email</label>
              <input name="guest_email" placeholder="optional" />
            </div>
          </div>
          <div class="row" style="margin-top:12px;">
            <div class="col">
              <button type="submit">Submit Tip</button>
            </div>
            <div class="col">
              <div id="classificationBadge" class="mini-badge">AI classification: waiting</div>
            </div>
          </div>
        </form>
      </div>

      <div class="card">
        <h3>Tip Queue</h3>
        <table>
          <thead><tr><th>Tip</th><th>Location</th><th>Status</th><th>Convert</th></tr></thead>
          <tbody id="tipTable"></tbody>
        </table>
      </div>
    </div>

    <div id="insights" class="tab-panel" style="display:none;">
      <div class="card">
        <h3>Reporting Dashboard</h3>
        <div id="chart"></div>
        <p id="insightSummary">Loading...</p>
      </div>
    </div>
  </div>

  <script src="/static/app.js"></script>
</body>
</html>
