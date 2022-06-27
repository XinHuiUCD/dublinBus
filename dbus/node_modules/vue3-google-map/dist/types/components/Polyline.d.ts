/// <reference types="google.maps" />
import { PropType } from "vue";
declare const _default: import("vue").DefineComponent<{
    options: {
        type: PropType<google.maps.PolylineOptions>;
        required: true;
    };
}, {
    polyline: import("vue").Ref<google.maps.Polyline | undefined>;
}, unknown, {}, {}, import("vue").ComponentOptionsMixin, import("vue").ComponentOptionsMixin, string[], string, import("vue").VNodeProps & import("vue").AllowedComponentProps & import("vue").ComponentCustomProps, Readonly<{
    options: google.maps.PolylineOptions;
} & {}>, {}>;
export default _default;
