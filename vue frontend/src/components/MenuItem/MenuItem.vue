<template>
	<div id="Menu" style="width: 20%;height: 750px; float: left;background: whitesmoke;">

		<div id="title">
			<h1 style="float: left;"><span style="color: black">Plan Your Journery</span>
				<span style="color:gray">With DublinBus</span>
			</h1>
			<div id="function">
				<!-- Your Position -->
				<el-input v-model="ur_position" class="w-50 m-2" placeholder="Your Position" :prefix-icon="Search"
					style="width: 80%;height: 40px;border-radius: 18px;margin-top: 20px; position: relative;" />

				<!-- Your Destination -->
				<el-input v-model="ur_destination" class="w-50 m-2" placeholder="Your Destination" :prefix-icon="Search"
					style="width: 80%;height: 40px;border-radius: 18px;margin-top: 20px; position: relative;" />


				<!-- Select date and time -->
				<div class="block">
					<el-date-picker size="large" v-model="select_time" type="datetime"
						placeholder="Select date and time" align="right" :picker-options="pickerOptions" clearable
						style="width: 80%;height: 40px;border-radius: 18px;margin-top: 20px;position: relative;">
					</el-date-picker>
				</div>


				<!-- test -->
				<div class="block2" style="margin-top: 50px; width: 80%;">
					<h4>Searching Information</h4>
					<el-timeline>
						<el-timeline-item v-for="(activity, index) in activities" :key="index" :icon="activity.icon"
							:type="activity.type" :color="activity.color" :size="activity.size"
							:hollow="activity.hollow" :timestamp="activity.timestamp">
							{{ activity.content }}
						</el-timeline-item>
					</el-timeline>
				</div>
			</div>
		</div>
	</div>

</template>

<script setup lang="ts">
	// import
	import {
		ref
	} from 'vue'
	import {
		Calendar,
		Search
	} from '@element-plus/icons-vue'
	import {
		MoreFilled
	} from '@element-plus/icons-vue'
	
	const ur_position = ref('')
	const ur_destination = ref('')
	const activities = [{
			content: 'Custom icon',
			timestamp: '2018-04-12 20:46',
			size: 'large',
			type: 'primary',
			icon: MoreFilled,
		},
		{
			content: 'Custom color',
			timestamp: '2018-04-03 20:46',
			color: '#0bbd87',
		},
		{
			content: 'Custom size',
			timestamp: '2018-04-03 20:46',
			size: 'large',
		},
		{
			content: 'Custom hollow',
			timestamp: '2018-04-03 20:46',
			type: 'primary',
			hollow: true,
		},
		{
			content: 'Default node',
			timestamp: '2018-04-03 20:46',
		},
	]
</script>

<style>
	.yp {
		width: 300px;
		height: 40px;
		border-radius: 18px;
		border: 1px solid #ccc;
		padding-left: 30px;
		position: relative;
		top: 20%;
		font-size: 20px;

	}

	.Destination {
		width: 300px;
		height: 40px;
		border-radius: 18px;
		border: 1px solid #ccc;
		padding-left: 30px;
		position: relative;
		top: 25%;
		font-size: 20px;
	}

	.Choose_Date_and_Time {
		width: 300px;
		height: 40px;
		border-radius: 18px;
		border: 1px solid #ccc;
		padding-left: 30px;
		position: relative;
		top: 30%;
		font-size: 20px;
	}
</style>
