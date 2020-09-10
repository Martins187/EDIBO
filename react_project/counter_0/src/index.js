import React from "react";
import ReactDOM from "react-dom";
import "./styles.css";

class CounterApp extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      count: 0
    };
  }

  handleIncrement() {
    this.setState({
      count: this.state.count + 1
    });
  }
  handleDecrement() {
    this.setState({
      count: this.state.count - 1
    });
  }
  handleReset() {
    this.setState({
      count: 0
    });
  }
  render() {
    return (
      <div class="container">
        <div class="counter">Counter</div>
        <div class="counter">{this.state.count}</div>
        <div>
          <button class="red button" onClick={() => this.handleDecrement()}>
            DECREASE
          </button>
          <button class="button" onClick={() => this.handleReset()}>
            RESET
          </button>
          <button CLASS="green button" onClick={() => this.handleIncrement()}>
            INCREASE
          </button>
        </div>
      </div>
    );
  }
}

ReactDOM.render(<CounterApp />, document.querySelector("#root"));
