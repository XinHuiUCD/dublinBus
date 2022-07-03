import { createStore } from 'vuex'
import ModuleUser from './user.js'


export default createStore({
	state: {
		map: null,
	},
	getters: {
	},
	mutations: {
		initMap(state, map) {
			state.map = map
		},
	},
	actions: {
	},
	modules: {
		user: ModuleUser,
	}
});

