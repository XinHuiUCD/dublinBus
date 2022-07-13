import { createStore } from 'vuex'
import ModuleUser from './user.js'


export default createStore({
	state: {
		// submit: null,
	},
	getters: {
	},
	mutations: {
		// functions(state,submit){
		// 	state.submit = submit
		// }
	},
	actions: {
	},
	modules: {
		user: ModuleUser,
	}
});

