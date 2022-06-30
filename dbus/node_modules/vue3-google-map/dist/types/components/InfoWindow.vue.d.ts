/// <reference types="google.maps" />
import { PropType } from "vue";
declare const _default: import("vue").DefineComponent<{
    options: {
        type: PropType<google.maps.InfoWindowOptions>;
        default: () => {};
    };
}, {
    infoWindow: import("vue").Ref<google.maps.InfoWindow | undefined>;
    infoWindowRef: import("vue").Ref<HTMLElement | undefined>;
    hasSlotContent: import("vue").ComputedRef<boolean | undefined>;
}, unknown, {}, {}, import("vue").ComponentOptionsMixin, import("vue").ComponentOptionsMixin, string[], string, import("vue").VNodeProps & import("vue").AllowedComponentProps & import("vue").ComponentCustomProps, Readonly<{
    options: google.maps.InfoWindowOptions;
} & {}>, {
    options: google.maps.InfoWindowOptions;
}>;
export default _default;
