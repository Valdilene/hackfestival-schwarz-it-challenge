import logo from './logo.svg';
import './App.css';
import ItemList from './components/Products/Products';

function App() {
  return (
    <div className="App">
      <header className="App-header">
      <main>
        <ItemList />  {/* Use the ItemList component */}
      </main>

      </header>
    </div>
  );
}

export default App;
