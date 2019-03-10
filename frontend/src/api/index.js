import axios from "axios";

const API_URL = "http://127.0.0.1:5000/api";

export function sinWaves(args) {
  return axios.post(`${API_URL}/v1/sin`, args);
}
