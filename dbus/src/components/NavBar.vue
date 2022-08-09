<template>
	<nav class="navbar navbar-expand-lg">
		<div class="container">
			<router-link class="navbar-brand" :to="{ name: 'home' }">
				<img src="https://z4a.net/images/2022/07/04/dublinBus.png" />
			</router-link>
			<button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarText"
				aria-controls="navbarText" aria-expanded="false" aria-label="Toggle navigation">
				<span class="navbar-toggler-icon"></span>
			</button>
			<div class="collapse navbar-collapse" id="navbarText">
				<ul class="navbar-nav me-auto mb-2 mb-lg-0">
					<li class="nav-item">
						<div class="card">
							<div class="card-body">
								<router-link class="nav-link active" aria-current="page" :to="{ name: 'home' }"
									style="color: #1dc1ec">Home
								</router-link>
							</div>
						</div>
					</li>
					<li class="nav-item">
						<div class="card">
							<div class="card-body">
								<router-link class="nav-link active" aria-current="page" :to="{ name: 'routeStopInfo' }"
									style="color: #1dc1ec">
									Route Info
								</router-link>
							</div>
						</div>
					</li>
					<li class="nav-item">
						<div class="card">
							<div class="card-body">
								<router-link class="nav-link active" aria-current="page" :to="{ name: 'weather' }"
									style="color: #1dc1ec">Weather
								</router-link>
							</div>
						</div>
					</li>

					<li class="nav-item">
						<div class="card">
							<div class="card-body">
								<router-link class="nav-link active" aria-current="page" :to="{ name: 'about' }"
									style="color: #1dc1ec">About Us
								</router-link>
							</div>
						</div>
					</li>

					<li class="nav-item">
						<div class="card">
							<div class="card-body">
								<router-link class="nav-link active" aria-current="page" :to="{ name: 'twitter' }"
									style="color: #1dc1ec">
									Twitter
								</router-link>
							</div>
						</div>
					</li>

				</ul>
				<ul class="navbar-nav" v-if="!$store.state.user.is_login">
					<li class="nav-item">
						<theme-button />
					</li>
					<li class="nav-item">
						<div class="card">
							<div class="card-body">
								<router-link class="nav-link active" :to="{ name: 'login' }" style="color: #1dc1ec">Log
									in</router-link>
							</div>
						</div>
					</li>
					<li class="nav-item">
						<div class="card">
							<div class="card-body">
								<router-link class="nav-link active" :to="{ name: 'register' }" style="color: #1dc1ec">
									Sign up</router-link>
							</div>
						</div>
					</li>
				</ul>
				<ul class="navbar-nav" v-else>
					<li class="nav-item">
						<theme-button />
					</li>
					<li class="nav-item">
						<div class="card showname">
							<div class="card-body">
								<router-link class="nav-link active" :to="{ name: 'home' }" style="color: #1dc1ec">
									Hi, {{ $store.state.user.username }}
								</router-link>
							</div>
						</div>
					</li>
					<li class="nav-item">
						<div class="card">
							<div class="card-body">
								<a class="nav-link active" style="cursor: pointer;" @click="logout">Exit</a>
							</div>
						</div>
					</li>
				</ul>
			</div>
		</div>
	</nav>
</template>

<script lang="ts">
/* eslint-disable */
import ThemeButton from "@/components/ThemeButton.vue";
import {
	ref
} from 'vue';
import {
	useStore
} from 'vuex';

const dark_mode = ref(false)

export default {
	name: "NavBar",
	data() {
		return {
			dark_mode
		}
	},
	setup() {
		const store = useStore();
		const logout = () => {
			store.commit("logout");
		};

		return {
			logout,
		}
	},
};
</script>

<style>
img {
	width: 200px;
}

.card {
	margin-left: 20px;
}

.card-body {
	padding: 2px 8px;
}

.showname {
	border: none;
}
</style>