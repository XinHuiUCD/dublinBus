import { PropType } from "vue";
import { MarkerClustererOptions, MarkerClustererEvents } from "@googlemaps/markerclusterer";
declare const _default: import("vue").DefineComponent<{
    options: {
        type: PropType<MarkerClustererOptions>;
        default: () => {};
    };
}, () => import("vue").VNode<import("vue").RendererNode, import("vue").RendererElement, {
    [key: string]: any;
}>[] | undefined, unknown, {}, {}, import("vue").ComponentOptionsMixin, import("vue").ComponentOptionsMixin, MarkerClustererEvents[], MarkerClustererEvents, import("vue").VNodeProps & import("vue").AllowedComponentProps & import("vue").ComponentCustomProps, Readonly<{
    options: MarkerClustererOptions;
} & {}>, {
    options: MarkerClustererOptions;
}>;
export default _default;
