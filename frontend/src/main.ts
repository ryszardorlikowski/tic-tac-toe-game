import {createApp} from 'vue'
import './style.css'
import App from './App.vue'
import {createPinia} from 'pinia'
import {Button, Form, Field, CellGroup, Col, Row, Popup, Cell, Divider, Notify, Tag, Grid, GridItem, Icon} from 'vant';
import 'vant/lib/index.css';
import {OpenAPI} from "./api/owi";

OpenAPI.BASE = import.meta.env.VITE_APP_BACKEND_URL ?? "http://localhost:5002"

const pinia = createPinia()
const app = createApp(App)
app.use(pinia)
app.use(Col);
app.use(Row);
app.use(Form);
app.use(Button);
app.use(Field);
app.use(CellGroup);
app.use(Popup);
app.use(Cell);
app.use(Divider);
app.use(Notify);
app.use(Tag);
app.use(Grid);
app.use(GridItem);
app.use(Icon);
app.mount('#app')
