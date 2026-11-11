import React from "react";
import ReactDOM from "react-dom/client";

function App() {
  return (
    <main>
      <h1>StockPilot</h1>
      <p>Inventory, procurement, and fulfillment workspace.</p>
      <p>Scaffold initialized. Implement the product workflows here.</p>
    </main>
  );
}

ReactDOM.createRoot(document.getElementById("root")!).render(
  <React.StrictMode><App /></React.StrictMode>,
);
